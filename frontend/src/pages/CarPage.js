import {CarsForm} from "../components/CarsForm";
import {Cars} from "../components/Cars";
import {Chat} from "../components/Chat";

const CarPage = () => {
    return (
        <div>
            <CarsForm/>
            <hr/>
            <Cars/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {CarPage};