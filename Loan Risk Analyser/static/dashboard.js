// =========================
// BAR CHART (Applications)
// =========================

const bar = document.getElementById("barChart");

if (bar) {
    new Chart(bar, {
        type: "bar",
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            datasets: [{
                label: "Loan Applications",
                data: [120, 180, 160, 220, 240, 280],
                backgroundColor: "#3da9fc"
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            }
        }
    });
}


// =========================
// PIE CHART (Risk Distribution)
// =========================

const pie = document.getElementById("pieChart");

if (pie) {

    const lowRisk = 60;
    const mediumRisk = 25;
    const highRisk = 15;

    new Chart(pie, {
        type: "pie",
        data: {
            labels: ["Low Risk", "Medium Risk", "High Risk"],
            datasets: [{
                data: [lowRisk, mediumRisk, highRisk],
                backgroundColor: [
                    "#22c55e",   // green
                    "#facc15",   // yellow
                    "#ef4444"    // red
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,   // 🔥 IMPORTANT for SMALL CHART
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}