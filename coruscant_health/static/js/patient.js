// Fonction pour charger les détails du patient


function loadPatientDetails(patientId) {
    fetch(`/doctor/get-patient-details/${patientId}/`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Patient not found');
            } else {
                const namePatient = document.getElementById('namePatient');
                document.getElementById('username').textContent = data.lastname + " " + data.firstname;
                document.getElementById('email').textContent = data.email;
                namePatient.value = data.lastname;
            }
        })
        .catch(error => console.error('Error:', error));
}

//getpatients
    function getPatient(){
        const patientId = this.getAttribute('data-id');
        console.log(patientId);
        loadPatientDetails(patientId);
    }

// Attachez l'événement de clic aux boutons
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click',  getPatient);
});

// Charger les détails du patient par défaut au chargement de la page pour l'ID 1
window.onload = function() {
    loadPatientDetails(1);
};