import { Link } from "react-router-dom";
import { Navbar, Nav, Container, Button } from "react-bootstrap";
import { useAuth } from "../Context/Authcontext";

export default function NavbarComponent() {
  const { user, logout } = useAuth();

  return (
    <Navbar collapseOnSelect expand="lg" bg="white" className="shadow-sm">
      <Container>
        {/* Use 'as={Link}' to keep it a Single Page App (no refresh) */}
        <Navbar.Brand as={Link} to="/" className="fw-bold">
          FastAPI Auth
        </Navbar.Brand>

        {/* The Toggle (hamburger) and Collapse are handled automatically */}
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ms-auto align-items-lg-center">
            {user ? (
              <>
                <Nav.Link as={Link} to="/me">Profile</Nav.Link>
                <Button 
                  variant="outline-danger" 
                  className="ms-lg-2 mt-2 mt-lg-0" 
                  onClick={logout}
                >
                  Logout
                </Button>
              </>
            ) : (
              <>
                <Nav.Link as={Link} to="/login">Login</Nav.Link>
                <Button 
                  as={Link} 
                  to="/register" 
                  variant="primary" 
                  className="ms-lg-2 mt-2 mt-lg-0"
                >
                  Register
                </Button>
              </>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
