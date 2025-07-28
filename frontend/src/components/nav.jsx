import React from "react";

function SideNavigation({ onSelect }) {
  const menuItems = [
    { id: "dashboard", label: "Dashboard" },
    { id: "clients", label: "Clients" },
    { id: "services", label: "Services" },
    { id: "booking", label: "Booking" },
    { id: "transactions", label: "Transactions" },
  ];

  return (
    <div className="h-screen w-64 bg-gray-800 text-white flex flex-col">
      <div className="p-4 text-2xl font-bold border-b border-gray-700">
        Alexis Services
      </div>
      <nav className="flex-1 p-4">
        <ul className="space-y-4">
          {menuItems.map((item) => (
            <li key={item.id}>
              <div
                onClick={() => onSelect(item.id)}
                className="block py-2 px-4 hover:bg-gray-700 rounded cursor-pointer"
              >
                {item.label}
              </div>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
}

export default SideNavigation;