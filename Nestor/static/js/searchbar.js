
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
		parent.getElementsByClassName("searchbar-input")[0].classList.add("searchbar-active");


		// elem.target.nextElementSibling.classList.remove("hidden");
		// elem.target.nextElementSibling.nextElementSibling.classList.add("active");
	}
});


const search = (id) => {
	const searchbar = document.getElementById(id);

	//get items in dropdown
	const item_list = searchbar.nextElementSibling;
	searchbar.addEventListener("keyup", (event) => {
		Array.from(item_list.childNodes).forEach((item) => {
			if (item.nodeType === Node.ELEMENT_NODE) {
				console.log(item);
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






