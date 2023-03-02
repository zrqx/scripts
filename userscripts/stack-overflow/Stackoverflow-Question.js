// ==UserScript==
// @name         Stackoverflow Question
// @namespace    http://homepage.com
// @version      0.1
// @description  Description
// @author       Author
// @match        https://stackoverflow.com/questions/*/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=stackoverflow.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Hide Elements
    const elements = ['#announcement-banner','.js-sticky-leftnav','#sidebar']
	elements.forEach( id => { document.querySelector(id).remove() })

	// Styles
	const styleInfo = [
		['#content','border-left: none'] // Remove the Left Border
	]
	styleInfo.forEach (async style => {
		element = await document.body.querySelector(style[0])
		element.style = style[1]
		console.log('ok')
	})
	
})();