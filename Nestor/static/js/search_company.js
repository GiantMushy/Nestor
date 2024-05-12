


const categories_list = document.getElementById('categories-list')
const countries_list = document.getElementById('countries-list')
const company_search = document.getElementById('search-company')

const search_btn_company = document.getElementById('search-btn-company')




const get_selected_items = (dropdown_list) => {
	let selected_items = []
	// Selecting all checkboxes in the category list
	let checkboxes = dropdown_list.querySelectorAll('input[type="checkbox"]')
	checkboxes.forEach((checkbox) => {
		if (checkbox.checked) {
			selected_items.push(checkbox.value)
		}
	})
	return selected_items
}
const search_for_companies = () => {
    const selected_categories = get_selected_items(categories_list)
    const selected_countries = get_selected_items(countries_list)

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


search_btn_company.addEventListener('click', (elem) => {
    search_for_companies()

});
