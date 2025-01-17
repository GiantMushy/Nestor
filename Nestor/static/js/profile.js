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

const toggleEditSkills = () => {
	const view = document.getElementById(`skills/view`);
	if (view.classList.contains("hidden")) { view.classList.remove("hidden") }
	else { view.classList.add("hidden") }
	const edit = document.getElementById(`skills/edit`);
	if (edit.classList.contains("hidden")) { edit.classList.remove("hidden") }
	else { edit.classList.add("hidden") }
}


const filterZips = (filter) => {
	const zip_dropdown = document.getElementById("id_zipcode");
	console.log(filter)
	const zips = zip_dropdown.getElementsByTagName("option")
	Array.from(zips).forEach((zip) => {
		if (zip.dataset.country !== filter) {
			zip.classList.add("hidden");
		} else if (zip.classList.contains("hidden")) {
			zip.classList.remove("hidden");
		}
	})
}



document.addEventListener('DOMContentLoaded', () => {
	const country_dropdown = document.getElementById("country-dropdown");
	country_dropdown.addEventListener('change', () => {
		document.getElementById("id_zipcode").value = "";
		const country = country_dropdown.value;
		filterZips(country);
	});


});
