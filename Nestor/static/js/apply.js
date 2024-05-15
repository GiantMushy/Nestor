const goTo = (window) => {
	const exp = document.getElementById('experience')
	if (window == 'experience') {if (exp.classList.contains("hidden")) {exp.classList.remove("hidden")}}
	else {if (exp.classList.contains("hidden")) {} else {exp.classList.add("hidden")}}

	const edu = document.getElementById('education')
	if (window == 'education') {if (edu.classList.contains("hidden")) {edu.classList.remove("hidden")}}
	else {if (edu.classList.contains("hidden")) {} else {edu.classList.add("hidden")}}

	const ref = document.getElementById('reference')
	if (window == 'reference') {if (ref.classList.contains("hidden")) {ref.classList.remove("hidden")}}
	else {if (ref.classList.contains("hidden")) {} else {ref.classList.add("hidden")}}

	const skl = document.getElementById('skill')
	if (window == 'skill') {if (skl.classList.contains("hidden")) {skl.classList.remove("hidden")}}
	else {if (skl.classList.contains("hidden")) {} else {skl.classList.add("hidden")}}

	const fnl = document.getElementById('final_review')
	if (window == 'final_review') {if (fnl.classList.contains("hidden")) {fnl.classList.remove("hidden")}}
	else {if (fnl.classList.contains("hidden")) {} else {fnl.classList.add("hidden")}}
}

const toggleAddInstance = (element) => {
	const view = document.getElementById(element + "/new");
	if (view.classList.contains("hidden")) { view.classList.remove("hidden") }
	else { view.classList.add("hidden") }
}