const toggleEditContactInfo = () => {
	const view = document.getElementById("contact-info-view");
	view.classList.add("hidden");
	const edit = document.getElementById("contact-info-edit");
	edit.classList.remove("hidden");
}

const toggleEditExperience = () => {
	const view = document.getElementById("experience-view");
	view.classList.add("hidden");
	const edit = document.getElementById("experience-edit");
	edit.classList.remove("hidden");
}

const toggleEditEducation = () => {
	const view = document.getElementById("education-view");
	view.classList.add("hidden");
	const edit = document.getElementById("education-edit");
	edit.classList.remove("hidden");
}

const toggleEditReference = () => {
	const view = document.getElementById("reference-view");
	view.classList.add("hidden");
	const edit = document.getElementById("reference-edit");
	edit.classList.remove("hidden");
}