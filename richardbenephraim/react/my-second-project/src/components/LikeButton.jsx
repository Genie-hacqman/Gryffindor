
import { useState } from "react";
const LikeButton = () => {

    const [likes, setLikes] = useState(0)
    return(
        <div>

<section>
{`${likes} ${likes !== 1 ? "likes" : "like"} `}
</section>

<section>

<button onClick={
    () => setLikes(likes+1)
}>
    like 
</button>
</section>
        </div>
    )
};

export default LikeButton;