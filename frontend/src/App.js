import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [cars, setCars] = useState([])

    useEffect(() => {
        axios.get('/api/cars').then(({data})=>setCars(data))
    }, []);

    return (
        <div>
            {
                cars.map(car=><div key={car.id}>{JSON.stringify(car)}</div>)
            }
        </div>
    );
};

export {App};