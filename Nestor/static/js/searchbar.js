
document.body.addEventListener("click", (elem) => {
	if (!elem.target.classList.contains("search-dropdown") && !elem.target.classList.contains("in-dropdown")) {
		const active_elements = document.getElementsByClassName("with-dropdown");
		//Make sure everything that is supposed to be hidden, is hidden
		Array.from(active_elements).forEach((i) => {
			const parent = i.parentNode;
			Array.from(parent.childNodes).forEach((baby) => {
				if (baby.nodeType === Node.ELEMENT_NODE) {
					if (!baby.classList.contains("hidden") && baby.classList.contains("search-dropdown")) {
						baby.classList.add("hidden");
					}
					if (baby.classList.contains("active")) {
						baby.classList.remove("active");
					}
					if (baby.classList.contains("searchbar-active")) {
						baby.classList.remove("searchbar-active");
					}
				}
			});
		});
	}
	if (elem.target.classList.contains("with-dropdown")) {
		const parent = elem.target.parentNode;
		parent.getElementsByClassName("chevron")[0].classList.add("active");
		parent.getElementsByClassName("search-dropdown")[0].classList.remove("hidden");
		if (parent.classList.contains("search-container")) {
			parent.getElementsByClassName("searchbar-input")[0].classList.add("searchbar-active");
		} else {
			document.getElementById("sort-btn").classList.add("searchbar-active");
		}
	}
});


const search = (id) => {
	const searchbar = document.getElementById(id);

	//get items in dropdown
	const item_list = searchbar.nextElementSibling;
	searchbar.addEventListener("keyup", (event) => {
		Array.from(item_list.childNodes).forEach((item) => {
			if (item.nodeType === Node.ELEMENT_NODE) {
				const search_term = item.id.toLowerCase()
				if (!search_term.startsWith(event.target.value.toLowerCase())) {
					item.style.display = "none";
				} else {
					item.style.display = "flex";
				}
			}
		})

	});
}


const get_selected_items = (dropdown_list) => {
	let selected_items = []
	let checkboxes = dropdown_list.querySelectorAll('input[type="checkbox"]')
	checkboxes.forEach((checkbox) => {
		if (checkbox.checked) {
			selected_items.push(checkbox.value)
		}
	})
	return selected_items
}

let current_sort = "";
document.addEventListener("DOMContentLoaded", () => {
	if (document.getElementById("all-jobs")) {
		sort("date", "jobs");
	} else {
		sort("company", "companies");
	}
});


const sort = (sort_by, selector) => {
	if (!document.getElementById("all-" + selector)) {
		return;
	}

	const all_items = document.getElementById("all-" + selector).childNodes;
	const clean = Array.from(all_items).filter(item => item.nodeType === Node.ELEMENT_NODE);

	//handle active arrow
	const active_arrow = document.getElementsByClassName("arrow-active")[0];
	if (active_arrow) {
		active_arrow.classList.remove("arrow-active");
		const rotated_arrow = document.getElementsByClassName("arrow-descend")[0];
		if (rotated_arrow) {
			rotated_arrow.classList.remove("arrow-descend");
		}
	}
	let sorted = [];

	if (sort_by === "job") {
		const job_arrow = document.getElementById("job-arrow");
		job_arrow.classList.add("arrow-active")
		//descend
		if (current_sort === "job-ascent") {
			job_arrow.classList.add("arrow-descend")
			sorted = clean.sort((b, a) => a.dataset.job.localeCompare(b.dataset.job))

			current_sort = "job-descent";
		} else {
			//ascend
			sorted = clean.sort((a, b) => a.dataset.job.localeCompare(b.dataset.job))
			current_sort = "job-ascent";
		}
	} else if (sort_by === "company") {
		const company_arrow = document.getElementById("company-arrow");
		company_arrow.classList.add("arrow-active")
		//descending
		if (current_sort === "company-ascent") {
			company_arrow.classList.add("arrow-descend")
			sorted = clean.sort((b, a) => a.dataset.company.localeCompare(b.dataset.company))

			current_sort = "company-descent";
		} else {
			//ascend
			sorted = clean.sort((a, b) => a.dataset.company.localeCompare(b.dataset.company))
			current_sort = "company-ascent";
		}
	} else if (sort_by === "date") {
		const date_arrow = document.getElementById("date-arrow");
		date_arrow.classList.add("arrow-active")
		//descending
		if (current_sort === "date-ascent") {
			date_arrow.classList.add("arrow-descend")
			sorted = clean.sort((a, b) => {
				let d1 = new Date(a.dataset.date)
				let d2 = new Date(b.dataset.date)
				return d2 - d1;
			})
			current_sort = "date-descent";
		} else {
			//ascend
			sorted = clean.sort((b, a) => {
				let d1 = new Date(a.dataset.date)
				let d2 = new Date(b.dataset.date)
				return d2 - d1;
			})
			current_sort = "date-ascent";
		}
	} else if (sort_by === "due") {
		const due_arrow = document.getElementById("due-arrow");
		due_arrow.classList.add("arrow-active")
		//descending
		if (current_sort === "due-ascent") {
			due_arrow.classList.add("arrow-descend")
			sorted = clean.sort((b, a) => a.dataset.due - b.dataset.due)

			current_sort = "due-descent";
		} else {

			//ascend
			sorted = clean.sort((a, b) => a.dataset.due - b.dataset.due)
			current_sort = "due-ascent";
		}
	}


	for (let i = 0; i < sorted.length; i++) {
		sorted[i].style.order = i;
	}
}


const get_updated_placeholder = (dropdown) => {
	let new_placeholder = ''
	dropdown.forEach((item) => {
		const item_name = item.querySelector('label').innerText
		const checkbox = item.querySelector("input[type='checkbox']")
		if (checkbox.checked) {
			new_placeholder += item_name + ', '
		}
	})
	new_placeholder = new_placeholder.replace(/, $/, '')
	return new_placeholder
}


const update_placeholder = (placeholder, html_item) => {
	html_item.value = placeholder
}

