console.log("[script.js] RUNNING");

const store_location = document.getElementById("location");
const store_name = document.getElementById("store_name");

document.getElementById("submit_button").addEventListener("click", async () => {
    await fetch("/stores/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            store_name: store_name.value,
            location: store_location.value
        })
    });
    console.log({"success": true});
});