    let todoItems = [];

    function renderTodoList() {
        const listItems = document.getElementById('list-items');
        listItems.innerHTML = '';

        todoItems.forEach((item, index) => {
        const listItem = document.createElement('p');
        listItem.className = 'todo-item';
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = item.done;
        checkbox.addEventListener('change', () => toggleDone(index));
        const text = document.createTextNode(item.text);
        const deleteButton = document.createElement('button');
        deleteButton.addEventListener('click', () => deleteItem(index));

        listItem.appendChild(checkbox);
        listItem.appendChild(text);
        listItem.appendChild(deleteButton);
        listItems.appendChild(listItem);
});
}

    function addItem() {
    const input = document.getElementById('todo-input');
    const text = input.value.trim();
    if (text !== '') {
    todoItems.push({ text, done: false });
    input.value = '';
    renderTodoList();
}
}

    function toggleDone(index) {
    todoItems[index].done = !todoItems[index].done;
    renderTodoList();
}

    function deleteItem(index) {
    todoItems.splice(index, 1);
    renderTodoList();
}

    renderTodoList();