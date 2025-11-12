import { BrowserRouter, Routes, Route, NavLink } from "react-router";

import Dashboard from "./pages/dashboard";
import "./stylesheets/main.scss";

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <nav className="navbar">
        <div className="left-tabs">
          <NavLink
            to="/"
            end
            className={({ isActive }) => (isActive ? "tab active" : "tab")}
          >
            Dashboard
          </NavLink>
          <NavLink
            to="/income"
            end
            className={({ isActive }) => (isActive ? "tab active" : "tab")}
          >
            Income
          </NavLink>
        </div>
      </nav>
      <main>
        <Routes>
          <Route path="/" element={<Dashboard />}></Route>
        </Routes>
      </main>
    </BrowserRouter>
  );
};

export default App;
