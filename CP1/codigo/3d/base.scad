// ============================================================
// SUNFOUNDER PICAR-V
// UPPER PLATE - PEÇA Nº 1
// ============================================================
//
// Modelo paramétrico baseado na geometria da Upper Plate
// apresentada na documentação do SunFounder PiCar-V.
//
// UNIDADE: mm
//
// ATENÇÃO:
// A SunFounder não publica um desenho técnico cotado da placa.
// As dimensões abaixo são uma reconstrução proporcional da peça.
// Para fabricação 1:1, validar com a peça física/CAD original.
//
// ============================================================


// ============================================================
// PARÂMETROS PRINCIPAIS
// ============================================================

comprimento = 260;
largura     = 140;
espessura   = 3;


// Furos de montagem
furo_m3 = 3.2;
furo_m25 = 2.8;


// Furos pequenos
furo_pequeno = 3.2;


// Rasgos
largura_rasgo = 4;
comprimento_rasgo = 18;


// Qualidade dos círculos
$fn = 48;


// ============================================================
// FUNÇÃO PARA FURO
// ============================================================

module furo(x, y, diametro) {

    translate([x, y, -1])
        cylinder(
            h = espessura + 2,
            d = diametro,
            $fn = 48
        );
}


// ============================================================
// RASGO RETANGULAR COM CANTOS ARREDONDADOS
// ============================================================

module rasgo(x, y, comprimento, largura) {

    translate([x, y, -1])
        hull() {

            translate([
                -comprimento/2 + largura/2,
                0
            ])
                cylinder(
                    h = espessura + 2,
                    d = largura,
                    $fn = 32
                );

            translate([
                comprimento/2 - largura/2,
                0
            ])
                cylinder(
                    h = espessura + 2,
                    d = largura,
                    $fn = 32
                );
        }
}


// ============================================================
// CONTORNO DA UPPER PLATE
// ============================================================
//
// Coordenadas centralizadas:
// X = largura
// Y = comprimento
//
// A frente fica na parte superior.
// ============================================================

module contorno() {

    polygon(points = [

        // ----------------------------------------------------
        // ABA SUPERIOR ESQUERDA
        // ----------------------------------------------------

        [-58, 130],
        [-42, 130],
        [-39, 127],
        [-39, 116],

        // Rebaixo central superior
        [-32, 109],

        // subida para aba direita
        [-30, 116],
        [-30, 127],
        [-27, 130],

        [27, 130],

        [30, 127],
        [30, 116],

        // rebaixo central
        [32, 109],

        [39, 116],
        [39, 127],
        [42, 130],

        [58, 130],

        // ----------------------------------------------------
        // TRANSIÇÃO PARA OS BRAÇOS LATERAIS
        // ----------------------------------------------------

        [60, 120],
        [68, 108],

        // braço direito
        [68, 98],
        [68, 92],

        [64, 86],
        [58, 82],

        // pescoço
        [42, 82],
        [34, 74],

        // abertura lateral direita
        [34, 57],
        [42, 49],

        // segundo braço direito
        [58, 49],
        [67, 43],

        [70, 36],
        [70, 28],

        [67, 21],
        [60, 17],

        // ----------------------------------------------------
        // CORPO PRINCIPAL
        // ----------------------------------------------------

        [58, 13],
        [58, -102],

        // canto inferior direito
        [55, -108],
        [49, -112],

        // fundo
        [-49, -112],
        [-55, -108],
        [-58, -102],

        // corpo esquerdo
        [-58, 13],

        // ----------------------------------------------------
        // BRAÇO INFERIOR ESQUERDO
        // ----------------------------------------------------

        [-60, 17],
        [-67, 21],
        [-70, 28],

        [-70, 36],
        [-67, 43],
        [-58, 49],

        [-42, 49],

        // abertura lateral esquerda
        [-34, 57],
        [-34, 74],

        [-42, 82],

        [-58, 82],

        [-64, 86],
        [-68, 92],

        [-68, 98],

        [-68, 108],
        [-60, 120]

    ]);
}


// ============================================================
// BASE PRINCIPAL
// ============================================================

difference() {

    // --------------------------------------------------------
    // PLACA
    // --------------------------------------------------------

    linear_extrude(height = espessura)
        contorno();


    // ========================================================
    // FUROS DA REGIÃO SUPERIOR
    // ========================================================

    // Aba superior esquerda
    furo(-47, 119, furo_m25);

    // Aba superior direita
    furo(47, 119, furo_m25);


    // Furo central superior
    furo(0, 103, furo_pequeno);


    // ========================================================
    // FUROS DOS BRAÇOS LATERAIS
    // ========================================================

    // Braço esquerdo - interno
    furo(-58, 39, furo_m3);

    // Braço esquerdo - externo
    furo(-68, 34, furo_m3);

    // Braço direito - interno
    furo(58, 39, furo_m3);

    // Braço direito - externo
    furo(68, 34, furo_m3);


    // ========================================================
    // FUROS DE TRANSIÇÃO DO CHASSI
    // ========================================================

    furo(-38, 70, furo_m3);
    furo(38, 70, furo_m3);


    // ========================================================
    // FUROS / FIXAÇÃO DA REGIÃO CENTRAL
    // ========================================================

    // esquerda
    furo(-38, 30, furo_m3);

    // direita
    furo(38, 30, furo_m3);

    // central
    furo(0, 25, furo_m3);


    // ========================================================
    // RASGOS HORIZONTAIS - CONJUNTO SUPERIOR
    // ========================================================

    rasgo(-30, 30, comprimento_rasgo, largura_rasgo);
    rasgo(30, 30, comprimento_rasgo, largura_rasgo);

    rasgo(-30, 21, comprimento_rasgo, largura_rasgo);
    rasgo(30, 21, comprimento_rasgo, largura_rasgo);


    // ========================================================
    // FURO CENTRAL DO CHASSI
    // ========================================================

    furo(0, -2, furo_m3);


    // ========================================================
    // FURO CENTRAL INFERIOR
    // ========================================================

    furo(0, -48, furo_m3);


    // ========================================================
    // FUROS LATERAIS DA REGIÃO INFERIOR
    // ========================================================

    furo(-42, -55, furo_m3);
    furo(42, -55, furo_m3);


    // ========================================================
    // RASGOS INFERIORES
    // ========================================================

    rasgo(-30, -57, comprimento_rasgo, largura_rasgo);
    rasgo(30, -57, comprimento_rasgo, largura_rasgo);

    rasgo(-30, -67, comprimento_rasgo, largura_rasgo);
    rasgo(30, -67, comprimento_rasgo, largura_rasgo);


    // ========================================================
    // FUROS PRÓXIMOS À BATERIA
    // ========================================================

    furo(-45, -83, furo_m3);
    furo(45, -83, furo_m3);

    furo(-25, -90, furo_m3);
    furo(25, -90, furo_m3);


    // ========================================================
    // ABERTURAS RETANGULARES LATERAIS
    // ========================================================

    translate([-43, -82, -1])
        cube([
            13,
            25,
            espessura + 2
        ]);

    translate([30, -82, -1])
        cube([
            13,
            25,
            espessura + 2
        ]);


    // ========================================================
    // ABERTURAS INFERIORES
    // ========================================================

    translate([-30, -101, -1])
        cube([
            13,
            17,
            espessura + 2
        ]);

    translate([17, -101, -1])
        cube([
            13,
            17,
            espessura + 2
        ]);

}