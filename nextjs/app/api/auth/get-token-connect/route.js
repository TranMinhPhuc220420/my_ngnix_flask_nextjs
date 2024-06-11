import axios from "axios";

export async function POST(request, context) {
    return Response.json({
        token: 'hello_world'
    })
}
