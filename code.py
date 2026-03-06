from manim import *

class Demo(Scene):
    def construct(self):
        title = Text("Simple Calculus Problem",
                     font_size=20)
        title.to_edge(UP)

        title001 = Text("Finding Absolute Extrema")
        
        self.play(Write(title))
        self.wait(1)

        self.play(Write(title001))
        self.play(title001.animate.move_to(ORIGIN))

        box = SurroundingRectangle(title001, color=GOLD, buff=0.2)
        self.play(Create(box))

        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(title001),
            FadeOut(box),
            run_time=0.5
        )
        
        equation = MathTex(r"C(t) = \frac{0.1t}{(t + 3)^2}",
                           font_size=48,
                           substrings_to_isolate=["C(t)"]
                           )
        equation.move_to(ORIGIN)

        self.play(Write(equation), run_time=2)
        self.play(
            equation.animate.scale(2),
            run_time=2
        )

        line1 = Text(
            "The concentration, C(t), in milligrams per cubic centimeter,",
        color=YELLOW,
        font_size=24
        )
        line2 = Text(
            "of a certain medicine in a patient's bloodstream",
            color=YELLOW,
            font_size=24
        )

        description = VGroup(line1, line2).arrange(DOWN, center=True, buff=0.3)
        description.next_to(equation, DOWN, buff=0.8)

        self.play(
            equation.animate.set_color_by_tex("C(t)", YELLOW),
            Write(description),
            run_time=3
        )
        self.wait(3)

        self.play(FadeOut(description), run_time=2)

        time_description = Text(
                "where, t, is the number of hours after the medicine is taken",
                color=BLUE,
                font_size=24
        )
        
        condition = MathTex(r"s.t \quad 1 \leq t \leq 6",
                            color=BLUE,
                            font_size=40)
        
        description02 = VGroup(time_description, condition).arrange(DOWN, center=True, buff=0.3)
        description02.next_to(equation, DOWN, buff=0.8)

        self.play(equation.animate.set_color_by_tex("t", BLUE),
                  Write(description02),
                  run_time=3)

        self.wait(3)

        self.play(FadeOut(description02),
                  equation.animate.set_color(WHITE),
                  run_time=2)
        
        first_step = Text("1. Determine Critical Points of C(t)",
                          font_size=45,
                          color=RED)
        first_step.to_edge(UP)

        self.play(Write(first_step), run_time=1)
        self.wait(2)
        self.play(FadeOut(first_step),
                  equation.animate.scale(0.5).move_to(ORIGIN))

        eq1 = MathTex(
            r"C'(t) = 0.1t(t + 3)^{-2}",
            font_size=48)

        eq2 = MathTex(
            r"C'(t) = 0.1t(t + 3)^{-2} + 0.1 \cdot (-2)(t + 3)^{-3}",
            font_size=48)
        
        eq3 = MathTex(
            r"C'(t) = 0.1(t + 3)^{-3}[(t + 3) - 2t]",
            font_size=48
        )
        
        eq4 = MathTex(
            r"C'(t) = \frac{0.1(3 - t)}{(t + 3)^3}",
            font_size=48
        )

        self.play(
            ReplacementTransform(equation, eq1)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq1, eq2)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq2, eq3)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq3, eq4)
        )
        self.wait(1)

        box02 = SurroundingRectangle(eq4, color=RED, buff=0.3)
        self.play(Create(box02))
        self.wait(2)
        self.play(FadeOut(box02),
                  eq4.animate.scale(2).move_to(ORIGIN),
                  run_time=2)
        second_step = Text("2. Set Derivative, C'(t) = 0",
                          font_size=45,
                          color=GREEN_B)
        second_step.to_edge(UP)

        self.play(Write(second_step), run_time=1)
        self.wait(2)
        self.play(FadeOut(second_step))

        eq5 = MathTex(
            r"0 = \frac{0.1(3 - t)}{(t + 3)^3}",
            font_size=96
        )

        notice = Text("Evaluate the zeros of numerator",
                      font_size=40,
                      color=RED)
        notice.next_to(eq5, DOWN, buff=0.7)

        eq6 = MathTex(
            r"0 = 0.1(3 - t)",
            font_size=96
        )

        eq7 = MathTex(
            r"0 = 3 - t",
            font_size=96
        )

        eq8 = MathTex(
            r"t = 3",
            font_size=96
        )
        self.play(
            ReplacementTransform(eq4, eq5),
            run_time=2
        )
        self.wait(1)
        self.play(Write(notice), 
                  run_time=1)
        self.wait(1.5)
        self.play(FadeOut(notice), 
                  eq5.animate.set_color(WHITE),
                  run_time=1
                  )
        self.play(
            ReplacementTransform(eq5, eq6)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq6, eq7)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq7, eq8)
        )
        self.wait(1)
        box03 = SurroundingRectangle(eq8, color=GREEN_B, buff=0.3)
        self.play(Create(box03))
        self.wait(1)

        third_step = Text("3. Evaluate C(t) at t = 3",
                          font_size=45,
                          color=BLUE_C)
        third_step.to_edge(UP)
        equation = MathTex(r"C(t) = \frac{0.1t}{(t + 3)^2}",
                           font_size=96,
                           substrings_to_isolate=["C(t)"]
                           )
        self.play(FadeOut(box03))
        self.play(Write(third_step),
                  ReplacementTransform(eq8, equation),
                   run_time=1)
        self.wait(2)
        self.play(FadeOut(third_step))

        eq9 = MathTex(
            r"C(3) = \frac{0.1 \times 3}{((3) + 3)^2}",
            font_size=96,
        )
        eq10 = MathTex(
            r"C(3) = \frac{0.3}{(6)^2}",
            font_size=96,
        )
        eq11 = MathTex(
            r"C(3) = \frac{0.3}{36}",
            font_size=96,
        )
        eq12 = MathTex(
            r"C(3) = \frac{1}{120}",
            font_size=96,
        )
        self.play(
            ReplacementTransform(equation, eq9)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq9, eq10)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq10, eq11)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(eq11, eq12)
        )
        self.wait(2)


        
        self.wait(2)
        

        box_c3 = SurroundingRectangle(eq12, color=BLUE_C, buff=0.3)
        self.play(Create(box_c3))
        self.wait(1)
        self.play(FadeOut(box_c3))

        fourth_step = Text(
            "4. Evaluate End Behaviors",
            font_size=45,
            color=PURPLE
        )
        fourth_step.to_edge(UP)
        
        self.play(
            Write(fourth_step),
            eq12.animate.scale(0.5).to_edge(LEFT),
            run_time=1.5
        )
        self.wait(2)
        self.play(FadeOut(fourth_step))
        

        equation_fresh = MathTex(
            r"C(t) = \frac{0.1t}{(t + 3)^2}",
            font_size=60
        )
        equation_fresh.move_to(ORIGIN)
        
    
        evaluate_1 = Text("Evaluate at t = 1:", font_size=32, color=ORANGE)
        evaluate_1.to_edge(UP)
        
        self.play(Write(evaluate_1), Write(equation_fresh))
        self.wait(1)
        self.play(FadeOut(evaluate_1))
        
  
        eq13 = MathTex(
            r"C(1) = \frac{0.1 \times 1}{(1 + 3)^2}",
            font_size=60
        )
        eq13.move_to(ORIGIN)
        
        eq14 = MathTex(
            r"C(1) = \frac{0.1}{4^2}",
            font_size=60
        )
        eq14.move_to(ORIGIN)
        
        eq15 = MathTex(
            r"C(1) = \frac{0.1}{16}",
            font_size=60
        )
        eq15.move_to(ORIGIN)
        
        eq16 = MathTex(
            r"C(1) = \frac{1}{160}",
            font_size=60
        )
        eq16.move_to(ORIGIN)
        
        self.play(ReplacementTransform(equation_fresh, eq13))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq13, eq14))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq14, eq15))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq15, eq16))
        self.wait(1)
        
        box_c1 = SurroundingRectangle(eq16, color=PURPLE, buff=0.3)
        self.play(Create(box_c1))
        self.wait(1)
        

        self.play(
            FadeOut(box_c1),
            eq16.animate.to_edge(UP + LEFT),
            run_time=1
        )
        self.wait(1)
        

        equation_fresh2 = MathTex(
            r"C(t) = \frac{0.1t}{(t + 3)^2}",
            font_size=60
        )
        equation_fresh2.move_to(ORIGIN)
        
        evaluate_6 = Text("Evaluate at t = 6:", font_size=32, color=ORANGE)
        evaluate_6.to_edge(UP)
        
        self.play(Write(evaluate_6), Write(equation_fresh2))
        self.wait(1)
        self.play(FadeOut(evaluate_6))

        eq17 = MathTex(
            r"C(6) = \frac{0.1 \times 6}{(6 + 3)^2}",
            font_size=60
        )
        eq17.move_to(ORIGIN)
        
        eq18 = MathTex(
            r"C(6) = \frac{0.6}{9^2}",
            font_size=60
        )
        eq18.move_to(ORIGIN)
        
        eq19 = MathTex(
            r"C(6) = \frac{0.6}{81}",
            font_size=60
        )
        eq19.move_to(ORIGIN)
        
        eq20 = MathTex(
            r"C(6) = \frac{2}{270}",
            font_size=60
        )
        eq20.move_to(ORIGIN)
        
        eq21 = MathTex(
            r"C(6) = \frac{1}{135}",
            font_size=60
        )
        eq21.move_to(ORIGIN)
        
        self.play(ReplacementTransform(equation_fresh2, eq17))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq17, eq18))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq18, eq19))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq19, eq20))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq20, eq21))
        self.wait(1)

        box_c6 = SurroundingRectangle(eq21, color=PURPLE, buff=0.3)
        self.play(Create(box_c6))
        self.wait(1)
        
 
        self.play(
            FadeOut(box_c6),
            eq21.animate.to_edge(DOWN + LEFT),
            run_time=1
        )
        self.wait(1)

        fifth_step = Text(
            "5. Compare Values",
            font_size=45,
            color=GOLD
        )
        fifth_step.to_edge(UP)
        
        self.play(Write(fifth_step))
        self.wait(2)
        self.play(FadeOut(fifth_step))
        

        comparison_title = Text("Comparison:", font_size=32, color=GOLD)
        comparison_title.to_edge(UP)
        
        c1_result = MathTex(
            r"C(1) = \frac{1}{160} \approx 0.00625",
            font_size=40,
            color=GREEN
        )
        
        c3_result = MathTex(
            r"C(3) = \frac{1}{120} \approx 0.00833",
            font_size=40,
            color=BLUE
        )
        
        c6_result = MathTex(
            r"C(6) = \frac{1}{135} \approx 0.00741",
            font_size=40,
            color=ORANGE
        )
        
        comparison_group = VGroup(c1_result, c3_result, c6_result).arrange(
            DOWN, 
            buff=0.5
        )
        comparison_group.move_to(ORIGIN)
        
        self.play(
            Write(comparison_title),
            FadeOut(eq16),
            FadeOut(eq12),
            FadeOut(eq21)
        )
        
        self.play(Write(comparison_group))
        self.wait(2)
        

        max_box = SurroundingRectangle(c3_result, color=PURPLE, buff=0.2)
        self.play(Create(max_box))
        self.wait(1)
        

        conclusion = Text(
            "Absolute Maximum at t = 3",
            font_size=48,
            color=GOLD
        )
        conclusion.next_to(comparison_group, DOWN, buff=1)
        
        self.play(Write(conclusion))
        self.wait(3)
        
     
        self.play(
            c3_result.animate.scale(1.3),
            conclusion.animate.scale(1.2),
            max_box.animate.scale(1.3)
        )
        self.wait(3)

        self.play(
            FadeOut(conclusion),
            FadeOut(max_box),
            FadeOut(comparison_group),
            FadeOut(comparison_title)
        )

        
