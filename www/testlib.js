
let protocole = window.location.protocol;
let protocoleWS = "ws:";
if (protocole == "https:") {
    protocoleWS = "wss:";
}

function cache(noeud) {
    let test = noeud.parentNode.nextSibling;
    if (test.style.display == "flex") {
        test.style.display = "none";
    } else {
        test.style.display = "flex";
    }
}

function connexion(event, idres) {
	let formName = event.target.form.id.replace("$", "\\$");
    
	let resultat = document.querySelector("#"+idres+"\\$result");
    let text = document.querySelector("#"+idres+"\\$text");
    let button = document.querySelector("#"+idres+"\\$button");
    
    if (button.value == "Deconnecter") {
        let meth = event.target.form.id.substring(0, event.target.form.id.indexOf("$"));
        window[idres].close();
        delete window[meth];
        button.value = "Connecter";
        return;
    }
    
	let fields = document.querySelectorAll("#"+formName+" .param");
    let params = {};
    for (let e of fields) {
		if (e.type && e.type == "file") {
			let fic = e.files[0];
			params[e.name] = fic;
		} else {
			params[e.name] = e.value;
		}
    }
	
    let urls = document.querySelectorAll("#"+formName+" .url");
    let url = '';
    for (let e of urls) {
        if (e.value) {
            url += e.value;
        }
    }

	let uri = protocoleWS+'//'+window.location.hostname+':'+window.location.port+url;
    let data = "";
	for (let d of Object.keys(params)) {
		if (params[d] !== undefined) {
			data += "&"+escape(d)+"="+escape(params[d]);
		}
	}
	if (data.length != 1) {
		uri += "?"+data.substring(1);
	}

	console.info(uri);
	let s = new WebSocket(uri);
	s.onmessage = function (x) {
         resultat.value += "\n"+ x.data;
    };
	s.onopen = function () {
        console.info("button", button);
        button.value = "Deconnecter";
		s.send('hello from client');
	};
	s.onclose = (x) => console.info("CLOSED WS", x.data);
	s.onerror = (x) => console.info("ERROR WS", x.data);

    window[idres] = s;
    
    text.onkeyup = function (evt) {
        if (evt.keyCode == 13) {
            s.send(text.value);
            text.value = "";
        }
    };

    return false;
}

function soumission (event, idres) {
	let formName = event.target.form.id.replace("$", "\\$");
    idres = idres.replace("$", "\\$");
	document.querySelector("#"+idres).value = "";
	
    let urls = document.querySelectorAll("#"+formName+" .url");
    let url = '';
    for (let e of urls) {
        if (e.value) {
            url += e.value;
        }
    }

    let fields = document.querySelectorAll("#"+formName+" .param");
    let headers = document.querySelectorAll("#"+formName+" .header");
    let formMethod = document.querySelector("#"+formName+" .formMethod").value;

    let params = {};
    for (let e of fields) {
		if (e.type && e.type == "file") {
			let fic = e.files[0];
			params[e.name] = fic;
		} else {
			params[e.name] = e.value;
		}
    }
    let heads = {};
    for (let e of headers) {
        heads[e.name] = e.value;
    }
    let l = document.location;
    let uri = l.protocol+"//"+l.hostname+":"+l.port+url;
    console.info(formMethod, url, params, heads);
    console.info(uri);
    let data = null;

    let xhr = new XMLHttpRequest();
    xhr.onload = function (ev) {
        console.info(
			ev.target.status,
			ev.target.statusText,
			ev.target.responseType,
			ev.target.response,
			ev.target.getAllResponseHeaders(),
			ev.target);
		document.querySelector("#"+idres).value =
			ev.target.status+"\n"+
			"==================\n"+
			ev.target.getAllResponseHeaders()+"\n"+
			"==================\n"+
			ev.target.statusText+"\n"+
			ev.target.responseType+"\n"+
			"--------------------\n"+
			ev.target.response+"\n"+
			"--------------------\n"+
			"";
		
    };
    
    if (formMethod == "GET") {
        data = "";
        for (let d of Object.keys(params)) {
            if (params[d] !== undefined) {
                data += "&"+escape(d)+"="+escape(params[d]);
            }
        }
        uri += "?"+data.substring(1);
		data = null;
    } else {
        data = new FormData();
        for (let d of Object.keys(params)) {
            if (params[d] !== undefined) {
                data.append(d, params[d]);
            }
        }
    }
    xhr.open(formMethod, uri, true);

    for (let h of Object.keys(heads)) {
        xhr.setRequestHeader(h, heads[h]);
    }
    
    xhr.send(data);
    
    return false;
}

function traiteParametre(meth, url, label, objs, doc) {
    let res = '<form id="'+meth+'$form">';
    let tabs= url.replace(/[\\](.)/g, "$1").split(/[{]|[}]/);

    res += '<input class="formMethod" maxlength="6" type="text" value="'+label+'" pattern="'+label+'"></input> ';
    res += '<span class="url">'+tabs[0]+'</span>';
    res += '<input type="hidden" class="url" value="'+tabs[0]+'"/>';
    for (let i=1; i<tabs.length - 1; i+=2) {
	    res += '<input type="text" class="url" value="'+tabs[i]+'"/>';
        res += '<span class="url">'+tabs[i+1]+'</span>';
        res += '<input type="hidden" class="url" value="'+tabs[i+1]+'"/>';
    }

	for (let obj of objs) {
	  if (obj.type == 'path') {
		  continue;
	  }
      res += '<div class="parameter '+obj.type+'">'+obj.name+' <input name="'
            + obj.name+'" class="param '+obj.type+'" type="'+obj.type+'"'
            + ((obj.pattern)?' pattern="'+obj.pattern+'"':'')
            + ' title="'+obj.type+': '+((obj.pattern)?obj.pattern:'')+'"'
            + ((obj["default"])?(' value="'+obj["default"]+'"'):' required="required"')
            + '></input>';
        let gg = doc.match('@param[ \t]+'+obj.name+'[ \t]+([^\n]*)\n');
        if (gg.length == 2) {
            res += ' <span class="doc">'+gg[1]+'</span>';
        }
        res += '</div>';
    }
    if (doc.indexOf("@websocket") > -1) {
        res += '<br>Message <input type="text" id="'+meth+'$text"/>'
            + '<br><input type="button" value="'+'connecter'+'" id="'+meth+'$button"/ onclick="connexion(event, \''+meth+'\')"/>';
    } else {
        res += '<br><input type="button" value="'+'soumettre'+'" onclick="soumission(event, \''+meth+'$result\')"/>';
    }
	
	res += '</form><textarea class="result" id="'+meth+'$result"></textarea>';
	return res;
}

function init(tests) {
	let pane = document.querySelector("#pane");
	let res = '';
	for (let meth of Object.keys(tests)) {
        let test = tests[meth];
        let doc2 = test[3];
        if (doc2) {
            // doc2 = doc2.replace(/@param[^\n]*\n/g, '');
        }
		res += '<div>Action <span class="method" onclick="cache(this)">'+meth+'</span> : <span class="command">'+test[0]
			+ '</span> <span class="url">'+test[1]
			+ '</span><pre class="doc">'+doc2+'</pre></div><div class="test">';
		res += traiteParametre(meth, test[1], test[0], test[2], test[3]);
		res += '</div>';
	}
	pane.innerHTML = res;
}
