import React, { useState, useEffect } from "react";
import axios from "axios";
import constant from "../assets/constants.json";

function ClientManagement() {
  const [clients, setClients] = useState([]);
  const [newClient, setNewClient] = useState({
    first_name: "",
    last_name: "",
    address: "",
    contact: "",
    email: "",
  });
  const [editingClient, setEditingClient] = useState(null);

  // get clients
  const fetchClients = async () => {
    try {
      const response = await axios.post(`${constant.api_url}/view`, {
        query: `
        query MyQuery {
            getAllClients {
            address
            contact
            email
            firstName
            id
            lastName
            }
        } 
        `,
      });
      console.log("Fetched clients:", response.data.data.getAllClients);
      setClients(response.data.data.getAllClients || []);
    } catch (error) {
      console.error("Error fetching clients:", error);
    }
  };

  // Add client
  const handleAddClient = async () => {
    try {
      const response = await axios.post(
        `${constant.api_url}/clients`,
        newClient
      );
      console.log("Added client:", response.data);

      setClients([...clients, response.data]);
      setNewClient({
        first_name: "",
        last_name: "",
        address: "",
        contact: "",
        email: "",
      });
      fetchClients(); 
    } catch (error) {
      console.error("Error adding client:", error);
    }
  };

  // Update client
  const handleUpdateClient = async () => {
    try {
        const client_id = editingClient.id;
        delete editingClient.id; 
      const response = await axios.patch(
        `${constant.api_url}/clients/${client_id}`,
        editingClient
      );
      console.log("Updated client:", response.data);

      setClients(
        clients.map((client) =>
          client.id === editingClient.id ? response.data : client
        )
      );
      setEditingClient(null);
        fetchClients();
    } catch (error) {
      console.error("Error updating client:", error);
    }
  };

  useEffect(() => {
    fetchClients();
  }, []);

  return (
    <div className="p-8 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6">Client Management</h1>

      {/* Add Client Form */}
      <div className="mb-6 space-y-4">
        <input
          type="text"
          value={newClient.first_name}
          onChange={(e) =>
            setNewClient({ ...newClient, first_name: e.target.value })
          }
          placeholder="First Name"
          className="border border-gray-300 rounded px-4 py-2 w-64"
        />
        <input
          type="text"
          value={newClient.last_name}
          onChange={(e) =>
            setNewClient({ ...newClient, last_name: e.target.value })
          }
          placeholder="Last Name"
          className="border border-gray-300 rounded px-4 py-2 w-64"
        />
        <input
          type="text"
          value={newClient.address}
          onChange={(e) =>
            setNewClient({ ...newClient, address: e.target.value })
          }
          placeholder="Address"
          className="border border-gray-300 rounded px-4 py-2 w-64"
        />
        <input
          type="text"
          value={newClient.contact}
          onChange={(e) =>
            setNewClient({ ...newClient, contact: e.target.value })
          }
          placeholder="Contact"
          className="border border-gray-300 rounded px-4 py-2 w-64"
        />
        <input
          type="email"
          value={newClient.email}
          onChange={(e) =>
            setNewClient({ ...newClient, email: e.target.value })
          }
          placeholder="Email"
          className="border border-gray-300 rounded px-4 py-2 w-64"
        />
        <button
          onClick={handleAddClient}
          className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
        >
          Add Client
        </button>
      </div>

      {/* Client List */}
      <div>
        <h2 className="text-2xl font-semibold mb-4">Clients</h2>
        {clients.length > 0 ? (
          <ul className="space-y-2">
            {clients.map((client) => (
              <li
                key={client.id}
                className="bg-white p-4 rounded shadow border border-gray-200"
              >
                {editingClient && editingClient.id === client.id ? (
                  <div className="space-y-2">
                    <input
                      type="text"
                      value={editingClient.first_name}
                      onChange={(e) =>
                        setEditingClient({
                          ...editingClient,
                          first_name: e.target.value,
                        })
                      }
                      placeholder="First Name"
                      className="border border-gray-300 rounded px-4 py-2 w-64"
                    />
                    <input
                      type="text"
                      value={editingClient.last_name}
                      onChange={(e) =>
                        setEditingClient({
                          ...editingClient,
                          last_name: e.target.value,
                        })
                      }
                      placeholder="Last Name"
                      className="border border-gray-300 rounded px-4 py-2 w-64"
                    />
                    <input
                      type="text"
                      value={editingClient.address}
                      onChange={(e) =>
                        setEditingClient({
                          ...editingClient,
                          address: e.target.value,
                        })
                      }
                      placeholder="Address"
                      className="border border-gray-300 rounded px-4 py-2 w-64"
                    />
                    <input
                      type="text"
                      value={editingClient.contact}
                      onChange={(e) =>
                        setEditingClient({
                          ...editingClient,
                          contact: e.target.value,
                        })
                      }
                      placeholder="Contact"
                      className="border border-gray-300 rounded px-4 py-2 w-64"
                    />
                    <input
                      type="email"
                      value={editingClient.email}
                      onChange={(e) =>
                        setEditingClient({
                          ...editingClient,
                          email: e.target.value,
                        })
                      }
                      placeholder="Email"
                      className="border border-gray-300 rounded px-4 py-2 w-64"
                    />
                    <button
                      onClick={handleUpdateClient}
                      className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                    >
                      Save
                    </button>
                    <button
                      onClick={() => setEditingClient(null)}
                      className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600 ml-2"
                    >
                      Cancel
                    </button>
                  </div>
                ) : (
                  <div>
                    <p>
                      {client.firstName} {client.lastName} - {client.email}
                    </p>
                    <p>Contact: {client.contact}</p>
                    <p>Address: {client.address}</p>
                    <button
                      onClick={() =>
                        setEditingClient({
                          id: client.id,  
                          first_name: client.firstName,
                          last_name: client.lastName,
                          address: client.address,
                          contact: client.contact,
                          email: client.email,
                        })
                      }
                      className="bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600 mt-2"
                    >
                      Edit
                    </button>
                  </div>
                )}
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-600">No clients added yet.</p>
        )}
      </div>
    </div>
  );
}

export default ClientManagement;