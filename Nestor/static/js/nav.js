let profile_dropdown_shown = false;
const toggleDropdown = () => {
	const dropdown = document.getElementById("profile-dropdown");
	const chevron = document.getElementById("chevron-profile");
	chevron.classList.toggle("active");
	dropdown.classList.toggle("expand-down");
	if (!profile_dropdown_shown) {
		profile_dropdown_shown = true;
	} else {
		// dropdown.classList.add("hidden");
		// chevron.classList.remove("active");
		profile_dropdown_shown = false;

	}
}