document.addEventListener('DOMContentLoaded', () => {
    const ticketForm = document.getElementById('ticket-form');
    const ticketItems = document.getElementById('ticket-items');

    // Fetch and display tickets on page load
    fetchTickets()
        .then(tickets => {
            tickets.forEach(ticket => {
                const li = document.createElement('li');
                li.textContent = `${ticket.title}: ${ticket.description}`;
                ticketItems.appendChild(li);
            });
        })
        .catch(error => console.error(error));

    // Handle form submission
    ticketForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const ticket = {
            title: document.getElementById('ticket-title').value,
            description: document.getElementById('ticket-description').value
        };

        try {
            await createTicket(ticket);
            const li = document.createElement('li');
            li.textContent = `${ticket.title}: ${ticket.description}`;
            ticketItems.appendChild(li);
            ticketForm.reset(); // Clear the form
        } catch (error) {
            console.error(error);
        }
    });
});
