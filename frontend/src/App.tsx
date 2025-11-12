import { BrowserRouter, Routes, Route, NavLink } from "react-router";

import Dashboard from "./pages/dashboard";
import Income from "./pages/income";
import Expenditure from "./pages/expenditure";
import House from "./pages/house";
import Limits from "./pages/limits";
import "./stylesheets/main.scss";

const App: React.FC = () => {
  const navLinkClass = ({ isActive }: { isActive: boolean }) =>
    isActive ? "tab active" : "tab";

  return (
    <BrowserRouter>
      <nav className="navbar">
        <div className="left-tabs">
          <NavLink to="/" end className={navLinkClass}>
            Dashboard
          </NavLink>
          <NavLink to="/income" end className={navLinkClass}>
            Income
          </NavLink>
          <NavLink to="/expenditure" end className={navLinkClass}>
            Expenditure
          </NavLink>
          <NavLink to="/house" end className={navLinkClass}>
            House
          </NavLink>
          <NavLink to="/limits" end className={navLinkClass}>
            Limits
          </NavLink>
        </div>
      </nav>
      <main>
        <Routes>
          <Route path="/" element={<Dashboard />}></Route>
          <Route path="/income" element={<Income />}></Route>
          <Route path="/expenditure" element={<Expenditure />}></Route>
          <Route path="/house" element={<House />}></Route>
          <Route path="/limits" element={<Limits />}></Route>
        </Routes>
      </main>
    </BrowserRouter>
  );
};

export default App;
