const API_BASE_URL = 'http://localhost:8080/tickets';

async function fetchTickets() {
    const response = await fetch(API_BASE_URL);
    if (!response.ok) {
        throw new Error('Failed to fetch tickets');
    }
    return await response.json();
}

async function createTicket(ticket) {
    const response = await fetch(API_BASE_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(ticket)
    });
    
    if (!response.ok) {
        throw new Error('Failed to create ticket');
    }
    
    return await response.json();
}
