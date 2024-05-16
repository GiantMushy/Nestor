
const categories_list = document.getElementById('categories-list')
const countries_list_job = document.getElementById('countries-list')
const companies_list = document.getElementById('companies-list')
const job_search = document.getElementById('search-job')

const search_btn_job= document.getElementById('search-btn-job')

const search_for_jobs = () => {
	const selected_categories = get_selected_items(categories_list)
	const selected_companies = get_selected_items(companies_list)
	const selected_countries = get_selected_items(countries_list_job)

	let param_added = false
	let parameters = ""
	if (job_search.value) {
		parameters += "job=" + job_search.value
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

search_btn_job.addEventListener('click', () => {
	search_for_jobs()
});

countries_list_job.addEventListener("change", (event) => {
    if (event.target.matches("input[type='checkbox']")) {
		const all_items = countries_list_job.querySelectorAll(".dropdown-item")
		const new_placeholder = get_updated_placeholder(all_items)
		const country_dropdown_list = document.getElementById("filter-location")
		console.log(new_placeholder)
		update_placeholder(new_placeholder, country_dropdown_list)
    }
});

// Checking whenever there is a change in checked checkboxes in category-dropdown
categories_list.addEventListener("change", (event) => {
    if (event.target.matches("input[type='checkbox']")) {
		const all_items = categories_list.querySelectorAll(".dropdown-item")
		const new_placeholder = get_updated_placeholder(all_items)
		const category_dropdown_list = document.getElementById("filter-category")
		update_placeholder(new_placeholder, category_dropdown_list)
    }
});

// Checking whenever there is a change in checked checkboxes in company-dropdown
companies_list.addEventListener("change", (event) => {
    if (event.target.matches("input[type='checkbox']")) {
		const all_items = companies_list.querySelectorAll(".dropdown-item")
		const new_placeholder = get_updated_placeholder(all_items)
		const company_dropdown_list = document.getElementById("filter-company")
		update_placeholder(new_placeholder, company_dropdown_list)
    }
});

const search_bar_jobs = document.getElementById("search-job")

search_bar_jobs.addEventListener("keydown", (event) => {
	if (event.key === "Enter") {
		search_for_jobs()
	}
})
