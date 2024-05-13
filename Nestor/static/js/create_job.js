
// const input_image = () => {
// 	const input = document.getElementById("image-input");
// 	input.classList.toggle("hidden");
// }


const update_image = () => {
	let input = document.getElementById("id_job_image");
	const image = document.getElementById("job-image");
	const error_msg = document.getElementById("error-msg-image");
	if (input.value) {
		image.addEventListener("error", () => {
			image.src = '../static/images/empty_img.png';
			error_msg.classList.remove("hidden");
			input.value = "";
			setTimeout(() => {
				error_msg.classList.add("hidden");
			}, 5000);
		})
		image.src = input.value;
		// input_image();
		// setTimeout(() => {
		// 	if (valid_img) {
		// 	}
		//
		// }, 1500);
	}
}
