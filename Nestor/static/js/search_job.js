

const categories_list = document.getElementById('categories-list')
const countries_list = document.getElementById('countries-list')
const companies_list = document.getElementById('companies-list')
const job_search = document.getElementById('search-job')

const search_btn_job= document.getElementById('search-btn-job')


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
const search_for_jobs = () => {
	const selected_categories = get_selected_items(categories_list)
	const selected_companies = get_selected_items(companies_list)
	const selected_countries = get_selected_items(countries_list)

	console.log(selected_categories)
	console.log(selected_companies)
	console.log(selected_countries)
	console.log(job_search.value)

	// TODO: LAGA HER
	let param_added = false
	let parameters = ""
	if (job_search.value) {
		parameters += "&job=" + job_search.value
		param_added = true
	}
	if (selected_countries) {
		if (param_added) { parameters += '&'}
		parameters += selected_countries.map((country_id) => `cou=${country_id}`).join('&');
		param_added = true
	}
	if (selected_companies) {
		if (param_added) { parameters += '&'}
		parameters += selected_companies.map((company_id) => `com=${company_id}`).join('&');
		param_added = true
	}
	if (selected_categories) {
		if (param_added) { parameters += '&'}
		parameters += selected_categories.map((category_id) => `cat=${category_id}`).join('&');
	}

	window.location.href = '/jobs/?' + parameters
}

search_btn_job.addEventListener('click', (elem) => {
	search_for_jobs()
	console.log('sindreh')
});