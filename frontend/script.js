const API_URL = "http://127.0.0.1:8000";

function ajouterRevenu() {
    const montant = parseFloat(document.getElementById("revenu-montant").value);
    const description = document.getElementById("revenu-description").value;

    fetch(`${API_URL}/revenus`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ montant, description })
    })
    .then(res => res.json())
    .then(data => alert("Revenu ajouté ✅"))
    .catch(err => alert("Erreur: " + err));
}

function ajouterDepense() {
    const montant = parseFloat(document.getElementById("depense-montant").value);
    const description = document.getElementById("depense-description").value;
    const categorie = document.getElementById("depense-categorie").value;

    fetch(`${API_URL}/depenses`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ montant, description, categorie })
    })
    .then(res => res.json())
    .then(data => alert("Dépense ajoutée ✅"))
    .catch(err => alert("Erreur: " + err));
}

function calculerSolde() {
    fetch(`${API_URL}/solde`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("resultat-solde").textContent = "Solde: " + data.solde + " €";
        });
}