from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import water_jug_solver

class WaterJugView(APIView):
    def post(self, request):
        try:
            x_capacity = int(request.data.get('x_capacity'))
            y_capacity = int(request.data.get('y_capacity'))
            z_amount_wanted = int(request.data.get('z_amount_wanted'))
        except (TypeError, ValueError):
            return Response({"error": "All inputs must be positive integers"}, status=status.HTTP_400_BAD_REQUEST)

        if x_capacity <= 0 or y_capacity <= 0 or z_amount_wanted <= 0:
            return Response({"error": "All inputs must be positive integers"}, status=status.HTTP_400_BAD_REQUEST)

        solution = water_jug_solver(x_capacity, y_capacity, z_amount_wanted)
        return Response(solution, status=status.HTTP_200_OK)