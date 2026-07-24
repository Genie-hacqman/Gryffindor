import Logo from "../ui/logo"
import image1 from "../../assets/favicon.png"
import Navlinks from "./navlinks"

function Navbar() {
  return (
    <div>

      <section>
        {/* logo */}

    < Logo logoUrl={image1}/>
    
        <div>
          {/* navlinks */}
          < Navlinks link = "/" text={"home"}/>
          < Navlinks link = "/movies" text={"movies"}/>
          < Navlinks link = "/tvshows" text={"tv shows"}/>
          < Navlinks link = "/mylist" text={"mylist"}/>
          < Navlinks link = "/support" text={"support"}/>
        </div>

        <div>
          {/* call to action */}


        </div>
      </section>
      
    </div>
  )
}

export default Navbar
