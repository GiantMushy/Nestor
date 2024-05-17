const goTo = (window) => {
	if (typeof window === "object") { window = window.id }
	const con = document.getElementById('cover-letter')
	if (window == 'cover-letter') { if (con.classList.contains("hidden")) { con.classList.remove("hidden") } }
	else { if (con.classList.contains("hidden")) { } else { con.classList.add("hidden") } }

	const exp = document.getElementById('experience')
	if (window == 'experience') { if (exp.classList.contains("hidden")) { exp.classList.remove("hidden") } }
	else { if (exp.classList.contains("hidden")) { } else { exp.classList.add("hidden") } }

	const edu = document.getElementById('education')
	if (window == 'education') { if (edu.classList.contains("hidden")) { edu.classList.remove("hidden") } }
	else { if (edu.classList.contains("hidden")) { } else { edu.classList.add("hidden") } }

	const ref = document.getElementById('reference')
	if (window == 'reference') { if (ref.classList.contains("hidden")) { ref.classList.remove("hidden") } }
	else { if (ref.classList.contains("hidden")) { } else { ref.classList.add("hidden") } }

	const skl = document.getElementById('skill')
	if (window == 'skill') { if (skl.classList.contains("hidden")) { skl.classList.remove("hidden") } }
	else { if (skl.classList.contains("hidden")) { } else { skl.classList.add("hidden") } }

	const fnl = document.getElementById('final_review')
	if (window == 'final_review') { if (fnl.classList.contains("hidden")) { fnl.classList.remove("hidden") } }
	else { if (fnl.classList.contains("hidden")) { } else { fnl.classList.add("hidden") } }
}

const toggleAddInstance = (element) => {
	const view = document.getElementById(element + "/new");
	if (view.classList.contains("hidden")) { view.classList.remove("hidden") }
	else { view.classList.add("hidden") }
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
