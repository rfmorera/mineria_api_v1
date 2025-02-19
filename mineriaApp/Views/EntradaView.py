import json
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from mineriaApp.Models.MongoModels import PortalEntrada
from mineriaApp.Serializers.MongoSerializers import EntradaSerializer
from mineriaApp.Services.EntradaService import EntradaService
from mineriaApp.Services.PreprocessorService import PreprocessorService


class EntradaView(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Devuelve las entradas"""
        data = request.data

        if 'ids' in data.keys():
            ids = data['ids']
            ent_list = EntradaService.get_by_ids(ids)
            serializer = EntradaSerializer(ent_list, many=True)
        else:
            raise AttributeError("Falta el parámetro Ids o está vacio")

        return Response(serializer.data)

    def post(self, request):
        """Inserta entradas"""
        data = request.data

        entradas = []
        for r in data:
            if "type" in r.keys():
                if r["type"] == "portal":
                    entradas.append(PortalEntrada(content=r["content"],
                                                  fecha=datetime.datetime.strptime(r["fecha"], "%d/%m/%Y"),
                                                  etiquetas=r["etiquetas"],
                                                  fuente=r["fuente_id"]))

        entradas = PreprocessorService.preprocess(entradas)
        entradas_saved = EntradaService.save_opinions(entradas)

        ent_ids = [str(ent.id) for ent in entradas_saved]

        content = {"ids": ent_ids}
        return Response(content)
