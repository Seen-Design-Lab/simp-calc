function appendNumber(number) {
    const display = document.getElementById('display');
    display.value += number;
}

function appendOperator(operator) {
    const display = document.getElementById('display');
    display.value += operator;
}

function clearDisplay() {
    const display = document.getElementById('display');
    display.value = '';
}

function calculateResult() {
    const display = document.getElementById('display');
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = 'Error';
    }
}


async function calculate(operation, num1, num2) {
    const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ operation, num1, num2 })
    });
    const result = await response.text();
    document.getElementById('display').value = result;
}
