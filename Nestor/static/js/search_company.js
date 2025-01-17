
const countries_list_company = document.getElementById('countries-list')
const company_search = document.getElementById('search-company')
const search_btn_company = document.getElementById('search-btn-company')

const search_bar_companies = document.getElementById("search-company")

/* Search for companies based on selected countries and joins the Id's
* to the parameters that are sent with the companies/ href*/
const search_for_companies = () => {
    // const selected_categories = get_selected_items(categories_list)
    const selected_countries = get_selected_items(countries_list_company)

	let param_added = false
	let parameters = ""
	if (company_search.value) {
		parameters += "&com=" + company_search.value
		param_added = true
	}
	if (selected_countries) {
		if (param_added) { parameters += '&' }
		parameters += selected_countries.map((country_id) => `cou=${country_id}`).join('&');
	}

	window.location.href = '/companies/?' + parameters
	}


search_btn_company.addEventListener('click', () => {
    search_for_companies()
});


search_bar_companies.addEventListener("keydown", (event) => {
	if (event.key === "Enter") {
		search_for_companies()
	}
})


/* Checking whenever there is a change in checked checkboxes in countries-dropdown and
* calls functions to get the new placeholder and update it */
countries_list_company.addEventListener("change", (event) => {
    if (event.target.matches("input[type='checkbox']")) {
		const all_items = countries_list_company.querySelectorAll(".dropdown-item")
		const new_placeholder = get_updated_placeholder(all_items)
		const country_dropdown_list = document.getElementById("filter-location")
		country_dropdown_list.value = ''
		update_placeholder(new_placeholder, country_dropdown_list)
    }
});
