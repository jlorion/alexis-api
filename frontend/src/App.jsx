import { useState } from "react";
import SideNavigation from "./components/nav";
import ClientManagement from "./components/client";

function App() {
  const [selectedPage, setSelectedPage] = useState("dashboard");

  const renderContent = () => {
    switch (selectedPage) {
      case "dashboard":
        return <h2 className="text-2xl font-semibold">Dashboard Content</h2>;
      case "clients":
        return <div><ClientManagement /></div>;
      case "services":
        return <h2 className="text-2xl font-semibold">Services Content</h2>;
      case "booking":
        return <h2 className="text-2xl font-semibold">Booking Content</h2>;
      case "transactions":
        return <h2 className="text-2xl font-semibold">Transactions Content</h2>;
      default:
        return <h2 className="text-2xl font-semibold">Welcome to Alexis Services</h2>;
    }
  };

  return (
    <div className="flex">
      <SideNavigation onSelect={setSelectedPage} />

      <div className="flex-1 flex flex-col items-center justify-center min-h-screen bg-gray-100">
        <header className="mb-4">
          <h1 className="text-3xl font-bold">Alexis Services</h1>
        </header>
        <main className="text-center">{renderContent()}</main>
        <footer className="mt-8 text-sm text-gray-600">
          <p>&copy; 2025 Alexis Services. All rights reserved.</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
