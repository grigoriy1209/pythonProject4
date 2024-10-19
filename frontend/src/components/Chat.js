import {socketService} from "../services/socketService";
import {useEffect, useRef, useState} from "react";


const Chat = () => {
    const [room, setRoom] = useState(null)
    const roomInput = useRef();
    const [socketClient, setSocketClient] = useState(null)
    const [message, setMessage] = useState([])

    useEffect(() => {
        if(room){
            socketInit(room).then(client=>setSocketClient(client))
        }
    }, [room]);


    const  socketInit = async (room)=>{
        const {chat} = await socketService();
        const client = await chat(room);

        client.onopen = ()=>{
            console.log('chat socket connected');
        }
        client.onmessage = ({data})=>{
           const {message, user} = JSON.parse(data.toString());
           setMessage(prevState => [...prevState,{user, message}])
        }
        return client
    }
    const roomHandler = ()=>{
        setRoom(roomInput.current.value)
    }

    const handlerEnterKey =(e) =>{
        if(e.key === 'Enter'){
            socketClient.send(JSON.stringify({
                data:e.target.value,
                action:'send_message',
                request_id:new Date().getTime()
            }))
            e.target.value = ''
        }
    }

    return (
        <div>
            {
                !room
                ?
                    <div>
                        <input type="text" ref={roomInput}/>
                        <button onClick={roomHandler}>Go to room</button>
                    </div>
                    :
                    <div>
                        {message.map(msg =><div> {msg.user}: {msg.message}</div>)}
                        <input type='text' onKeyDown={handlerEnterKey}/>
                    </div>
            }
        </div>
    );
};

export {Chat};