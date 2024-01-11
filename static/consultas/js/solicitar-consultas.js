const especialidadeOption = document.querySelectorAll("#getProfissionais");
const profissionaisEspecialidade = document.getElementById("profissionaisEspecialidade");

async function buscarProfissionais(especialidade) {
    try {
        const url = "http://127.0.0.1:8000/especialidades/solicitar_profissionais/";
        const response = await fetch(url, {
            method: 'GET'
        });
        const data = await response.json();
        console.log(data);
        
        profissionaisEspecialidade.innerHTML = '';

        data.forEach(item => {
            if (especialidade === 'Cardiologista' && item.especialidades === 1) {
                const option = document.createElement('option');
                option.value = item.nome;
                option.text = item.nome;
                profissionaisEspecialidade.appendChild(option);
            } else if (especialidade === 'Endocrinologista' && item.especialidades === 2) {
                const option = document.createElement('option');
                option.value = item.nome;
                option.text = item.nome;
                profissionaisEspecialidade.appendChild(option); 
            }
        });
    } catch (error) {
        console.log('Error', error)
    }
};

function handleClickEspecialidade(event) {        
    const especialidadeSelecionada = event.target.innerText.trim()     
    buscarProfissionais(especialidadeSelecionada);            
};

for (let i = 0; i < especialidadeOption.length; i++) {
    especialidadeOption[i].addEventListener('click', handleClickEspecialidade);
}
