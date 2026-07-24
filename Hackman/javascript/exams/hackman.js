const container = document.getElementById("btnContainer");
const btn = document.createElement("button");
btn.textContent = "Click Me";
btn.className = "px-4 py-2 bg-black text-white rounded";

btn.addEventListener("click", function() {
    console.log("hello!");
});

container.appendChild(btn);
