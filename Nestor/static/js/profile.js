const toggleEditContactInfo = () => {
	const view = document.getElementById("contact-info/view");
	view.classList.add("hidden");
	const edit = document.getElementById("contact-info/edit");
	edit.classList.remove("hidden");
}


const toggleEditExperience = (id) => {
	const view = document.getElementById(`experience/view/${id}`);
	view.classList.add("hidden");
	const edit = document.getElementById(`experience/edit/${id}`);
	edit.classList.remove("hidden");
}
const toggleAddExperience = () => {
	const view = document.getElementById("experience/new");
	if (view.classList.contains("hidden")) { view.classList.remove("hidden") }
	else { view.classList.add("hidden") }
}
const removeExperience = (id) => {

}


const toggleEditEducation = (id) => {
	const view = document.getElementById(`education/view/${id}`);
	view.classList.add("hidden");
	const edit = document.getElementById(`education/edit/${id}`);
	edit.classList.remove("hidden");
}
const toggleAddEducation = () => {
	const view = document.getElementById("education/new");
	if (view.classList.contains("hidden")) { view.classList.remove("hidden") }
	else { view.classList.add("hidden") }
}
const removeEducation = (id) => {

}


const toggleEditReference = (id) => {
	const view = document.getElementById(`reference/view/${id}`);
	view.classList.add("hidden");
	const edit = document.getElementById(`reference/edit/${id}`);
	edit.classList.remove("hidden");
}
const toggleAddReference = () => {
	const view = document.getElementById("reference/new");
	if (view.classList.contains("hidden")) { view.classList.remove("hidden") }
	else { view.classList.add("hidden") }
}
const removeReference = (id) => {

}

const toggleEditSkills = () => {
	const view = document.getElementById(`skills/view`);
	if (view.classList.contains("hidden")) { view.classList.remove("hidden") }
	else { view.classList.add("hidden") }
	const edit = document.getElementById(`skills/edit`);
	if (edit.classList.contains("hidden")) { edit.classList.remove("hidden") }
	else { edit.classList.add("hidden") }
}

const removeSkill = () => {}
