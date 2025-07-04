function sortTable() {
    const table = document.getElementById("productTable");
    const rows = Array.from(table.rows).slice(1); // Exclude header row
    let isAscending = table.getAttribute("data-sort") !== "asc";
    table.setAttribute("data-sort", isAscending ? "asc" : "desc");

    rows.sort((row1, row2) => {
        const price1 = parseFloat(row1.cells[1].textContent.replace('$', ''));
        const price2 = parseFloat(row2.cells[1].textContent.replace('$', ''));
        return isAscending ? price1 - price2 : price2 - price1;
    });

    // Reorder rows in the table body
    const tbody = table.tBodies[0];
    tbody.append(...rows);
}