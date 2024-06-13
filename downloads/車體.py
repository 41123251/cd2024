# NX 1872
# Journal created by Admin on Thu Jun 13 14:04:18 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   功能表：檔案(F)->新建(N)...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "新建 對話方塊")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "ModelTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "模型"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "C:\\Users\\Admin\\Desktop\\model1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    # User Function call - UF_PART_ask_part_name
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder1.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId4, "建立草圖 對話方塊")
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XY plane")
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane2.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom1 = [NXOpen.NXObject.Null] * 1 
    geom1[0] = datumPlane1
    plane2.SetGeometry(geom1)
    
    plane2.SetFlip(False)
    
    plane2.SetExpression(None)
    
    plane2.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane2.Evaluate()
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane3.SynchronizeToPlane(plane2)
    
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom2 = [NXOpen.NXObject.Null] * 1 
    geom2[0] = datumPlane1
    plane3.SetGeometry(geom2)
    
    plane3.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane3.Evaluate()
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject2 = sketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject2
    feature1 = sketch1.Feature
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId7)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "建立草圖")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression4)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression3)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane3.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->矩形(R)...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    expression5 = workPart.Expressions.CreateSystemExpression("30")
    
    expression6 = workPart.Expressions.CreateSystemExpression("50")
    
    theSession.SetUndoMarkVisibility(markId9, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(-26.0, 44.0, 0.0)
    endPoint1 = NXOpen.Point3d(4.0, 44.0, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(4.0, 44.0, 0.0)
    endPoint2 = NXOpen.Point3d(4.0, -6.0, 0.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(4.0, -6.0, 0.0)
    endPoint3 = NXOpen.Point3d(-26.0, -6.0, 0.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(-26.0, -6.0, 0.0)
    endPoint4 = NXOpen.Point3d(-26.0, 44.0, 0.0)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = line3
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0
    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_3.Geometry = line4
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)
    
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_4.Geometry = line4
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0
    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)
    
    geom3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom3.Geometry = line1
    geom3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom3)
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint7 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)
    
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0
    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = line1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_1.Geometry = line1
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(-11.0, 33.965770379379293, 0.0)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, expression5, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = line2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimObject2_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_2.Geometry = line2
    dimObject2_2.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_2.AssocValue = 0
    dimObject2_2.HelpPoint.X = 0.0
    dimObject2_2.HelpPoint.Y = 0.0
    dimObject2_2.HelpPoint.Z = 0.0
    dimObject2_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(-6.0342296206207102, 19.0, 0.0)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, expression6, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 4 
    geoms2[0] = line1
    geoms2[1] = line2
    geoms2[2] = line3
    geoms2[3] = line4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketch2 = theSession.ActiveSketch
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("30")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId11, "拉伸 對話方塊")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(-10.694657175506086, -6.0, 0.0)
    section1.AddToSection(rules1, line3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId13, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId12, None)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("20")
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId14, None)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId15, None)
    
    theSession.SetUndoMarkName(markId11, "拉伸")
    
    expression9 = extrudeBuilder1.Limits.StartExtend.Value
    expression10 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression7)
    
    workPart.Expressions.Delete(expression8)
    
    scaleAboutPoint1 = NXOpen.Point3d(2.0649143825767911, 15.929339522735376, 0.0)
    viewCenter1 = NXOpen.Point3d(-2.0649143825767911, -15.929339522735376, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(7.079706454549056, 11.091540112126857, 0.0)
    viewCenter2 = NXOpen.Point3d(-7.079706454549056, -11.091540112126857, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(9.2508164339440899, 7.362894712731018, 0.0)
    viewCenter3 = NXOpen.Point3d(-9.2508164339440899, -7.362894712731018, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(8.9109905241257295, 5.1351470816995874, 0.0)
    viewCenter4 = NXOpen.Point3d(-8.9109905241257543, -5.1351470816995874, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(7.1287924193005621, 4.1081176653596687, 0.0)
    viewCenter5 = NXOpen.Point3d(-7.1287924193006136, -4.1081176653596687, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane4
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId16, "建立草圖 對話方塊")
    
    scalar1 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 130 * 170 {(4,44,20)(4,19,20)(4,-6,20) EXTRUDE(2)}")
    point2 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge2 = extrude1.FindObject("EDGE * 120 * 170 {(4,44,0)(4,19,0)(4,-6,0) EXTRUDE(2)}")
    direction3 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude1.FindObject("FACE 170 {(4,19,10) EXTRUDE(2)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction3, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane5.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom4 = [NXOpen.NXObject.Null] * 1 
    geom4[0] = face1
    plane5.SetGeometry(geom4)
    
    plane5.SetFlip(False)
    
    plane5.SetExpression(None)
    
    plane5.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane5.Evaluate()
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane6.SynchronizeToPlane(plane5)
    
    scalar2 = workPart.Scalars.CreateScalar(100.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point3 = workPart.Points.CreatePoint(edge1, scalar2, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane6.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom5 = [NXOpen.NXObject.Null] * 1 
    geom5[0] = face1
    plane6.SetGeometry(geom5)
    
    plane6.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane6.Evaluate()
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId17, None)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject3 = sketchInPlaceBuilder2.Commit()
    
    sketch3 = nXObject3
    feature3 = sketch3.Feature
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId19)
    
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId18, None)
    
    theSession.SetUndoMarkName(markId16, "建立草圖")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression12)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point3)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression11)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane4.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression14)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression13)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane6.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->矩形(R)...
    # ----------------------------------------------
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    expression15 = workPart.Expressions.CreateSystemExpression("5")
    
    expression16 = workPart.Expressions.CreateSystemExpression("20")
    
    theSession.SetUndoMarkVisibility(markId21, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint5 = NXOpen.Point3d(4.0, -5.9999999999999929, 20.0)
    endPoint5 = NXOpen.Point3d(4.0, -0.99999999999999289, 20.0)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    startPoint6 = NXOpen.Point3d(4.0, -0.99999999999999289, 20.0)
    endPoint6 = NXOpen.Point3d(4.0, -0.99999999999999289, 0.0)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    startPoint7 = NXOpen.Point3d(4.0, -0.99999999999999289, 0.0)
    endPoint7 = NXOpen.Point3d(4.0, -5.9999999999999929, 0.0)
    line7 = workPart.Curves.CreateLine(startPoint7, endPoint7)
    
    startPoint8 = NXOpen.Point3d(4.0, -5.9999999999999929, 0.0)
    endPoint8 = NXOpen.Point3d(4.0, -5.9999999999999929, 20.0)
    line8 = workPart.Curves.CreateLine(startPoint8, endPoint8)
    
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line7, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = line5
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_5.Geometry = line6
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = line6
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = line7
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint11 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    
    geom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_7.Geometry = line7
    geom1_7.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_7.SplineDefiningPointIndex = 0
    geom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_7.Geometry = line8
    geom2_7.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_7, geom2_7)
    
    geom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_8.Geometry = line8
    geom1_8.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_8.SplineDefiningPointIndex = 0
    geom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_8.Geometry = line5
    geom2_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_8, geom2_8)
    
    geom6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom6.Geometry = line5
    geom6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint14 = theSession.ActiveSketch.CreateHorizontalConstraint(geom6)
    
    conGeom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_5.Geometry = line5
    conGeom1_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_5.SplineDefiningPointIndex = 0
    conGeom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_5.Geometry = line6
    conGeom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_5, conGeom2_5)
    
    conGeom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_6.Geometry = line6
    conGeom1_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_6.SplineDefiningPointIndex = 0
    conGeom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_6.Geometry = line7
    conGeom2_6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint16 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_6, conGeom2_6)
    
    conGeom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_7.Geometry = line7
    conGeom1_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_7.SplineDefiningPointIndex = 0
    conGeom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_7.Geometry = line8
    conGeom2_7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint17 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_7, conGeom2_7)
    
    conGeom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_8.Geometry = line8
    conGeom1_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_8.SplineDefiningPointIndex = 0
    conGeom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_8.Geometry = line5
    conGeom2_8.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint18 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_8, conGeom2_8)
    
    geom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_9.Geometry = line5
    geom1_9.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_9.SplineDefiningPointIndex = 0
    geom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(3:1B)")
    point4 = datumCsys2.FindObject("POINT 1")
    geom2_9.Geometry = point4
    geom2_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint19 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_9, geom2_9)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = line5
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_3.Geometry = line5
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 0.0
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(4.0, -3.4999999999999929, 16.711983637915004)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_3, dimObject2_3, dimOrigin3, expression15, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint3
    dimension3 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = line6
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line6
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = 0.0
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = 0.0
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(4.0, -4.2880163620849876, 10.0)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_4, dimObject2_4, dimOrigin4, expression16, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    sketchHelpedDimensionalConstraint4 = sketchDimensionalConstraint4
    dimension4 = sketchHelpedDimensionalConstraint4.AssociatedDimension
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms3 = [NXOpen.SmartObject.Null] * 4 
    geoms3[0] = line5
    geoms3[1] = line6
    geoms3[2] = line7
    geoms3[3] = line8
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms3)
    
    geoms4 = [NXOpen.SmartObject.Null] * 4 
    geoms4[0] = line5
    geoms4[1] = line6
    geoms4[2] = line7
    geoms4[3] = line8
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms4)
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    expression17 = workPart.Expressions.CreateSystemExpression("5")
    
    theSession.SetUndoMarkVisibility(markId22, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint9 = NXOpen.Point3d(4.0, 44.0, 20.0)
    endPoint9 = NXOpen.Point3d(4.0, 39.0, 20.0)
    line9 = workPart.Curves.CreateLine(startPoint9, endPoint9)
    
    startPoint10 = NXOpen.Point3d(4.0, 39.0, 20.0)
    endPoint10 = NXOpen.Point3d(4.0, 39.0, -1.5)
    line10 = workPart.Curves.CreateLine(startPoint10, endPoint10)
    
    startPoint11 = NXOpen.Point3d(4.0, 39.0, -1.5)
    endPoint11 = NXOpen.Point3d(4.0, 44.0, -1.5)
    line11 = workPart.Curves.CreateLine(startPoint11, endPoint11)
    
    startPoint12 = NXOpen.Point3d(4.0, 44.0, -1.5)
    endPoint12 = NXOpen.Point3d(4.0, 44.0, 20.0)
    line12 = workPart.Curves.CreateLine(startPoint12, endPoint12)
    
    theSession.ActiveSketch.AddGeometry(line9, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line10, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line11, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line12, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_10.Geometry = line9
    geom1_10.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_10.SplineDefiningPointIndex = 0
    geom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_10.Geometry = line10
    geom2_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint20 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_10, geom2_10)
    
    geom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_11.Geometry = line10
    geom1_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_11.SplineDefiningPointIndex = 0
    geom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_11.Geometry = line11
    geom2_11.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint21 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_11, geom2_11)
    
    geom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_12.Geometry = line11
    geom1_12.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_12.SplineDefiningPointIndex = 0
    geom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_12.Geometry = line12
    geom2_12.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint22 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_12, geom2_12)
    
    geom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_13.Geometry = line12
    geom1_13.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_13.SplineDefiningPointIndex = 0
    geom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_13.Geometry = line9
    geom2_13.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint23 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_13, geom2_13)
    
    geom7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom7.Geometry = line9
    geom7.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint24 = theSession.ActiveSketch.CreateHorizontalConstraint(geom7)
    
    conGeom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_9.Geometry = line9
    conGeom1_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_9.SplineDefiningPointIndex = 0
    conGeom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_9.Geometry = line10
    conGeom2_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint25 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_9, conGeom2_9)
    
    conGeom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_10.Geometry = line10
    conGeom1_10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_10.SplineDefiningPointIndex = 0
    conGeom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_10.Geometry = line11
    conGeom2_10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint26 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_10, conGeom2_10)
    
    conGeom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_11.Geometry = line11
    conGeom1_11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_11.SplineDefiningPointIndex = 0
    conGeom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_11.Geometry = line12
    conGeom2_11.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint27 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_11, conGeom2_11)
    
    conGeom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_12.Geometry = line12
    conGeom1_12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_12.SplineDefiningPointIndex = 0
    conGeom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_12.Geometry = line9
    conGeom2_12.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint28 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_12, conGeom2_12)
    
    geom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_14.Geometry = line9
    geom1_14.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_14.SplineDefiningPointIndex = 0
    geom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_14.Geometry = edge1
    geom2_14.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint29 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_14, geom2_14)
    
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_5.Geometry = line9
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 0.0
    dimObject1_5.HelpPoint.Y = 0.0
    dimObject1_5.HelpPoint.Z = 0.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimObject2_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_5.Geometry = line9
    dimObject2_5.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_5.AssocValue = 0
    dimObject2_5.HelpPoint.X = 0.0
    dimObject2_5.HelpPoint.Y = 0.0
    dimObject2_5.HelpPoint.Z = 0.0
    dimObject2_5.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(4.0, 41.5, 23.288016362084996)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_5, dimObject2_5, dimOrigin5, expression17, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    sketchHelpedDimensionalConstraint5 = sketchDimensionalConstraint5
    dimension5 = sketchHelpedDimensionalConstraint5.AssociatedDimension
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_6.Geometry = line10
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 0.0
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimObject2_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_6.Geometry = line10
    dimObject2_6.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_6.AssocValue = 0
    dimObject2_6.HelpPoint.X = 0.0
    dimObject2_6.HelpPoint.Y = 0.0
    dimObject2_6.HelpPoint.Z = 0.0
    dimObject2_6.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(4.0, 35.711983637915004, 9.25)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_6, dimObject2_6, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint6 = sketchDimensionalConstraint6
    dimension6 = sketchHelpedDimensionalConstraint6.AssociatedDimension
    
    expression18 = sketchHelpedDimensionalConstraint6.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms5 = [NXOpen.SmartObject.Null] * 4 
    geoms5[0] = line9
    geoms5[1] = line10
    geoms5[2] = line11
    geoms5[3] = line12
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms5)
    
    geoms6 = [NXOpen.SmartObject.Null] * 4 
    geoms6[0] = line9
    geoms6[1] = line10
    geoms6[2] = line11
    geoms6[3] = line12
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms6)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.DeleteUndoMark(markId23, "Create Rectangle")
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    geom1_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_15.Geometry = line12
    geom1_15.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_15.SplineDefiningPointIndex = 0
    geom2_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_15.Geometry = line2
    geom2_15.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_15.SplineDefiningPointIndex = 0
    sketchGeometricConstraint30 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_15, geom2_15)
    
    theSession.SetUndoMarkVisibility(markId25, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    parallelDimension1 = dimension6
    theSession.UpdateManager.LogForUpdate(parallelDimension1)
    
    startPoint13 = NXOpen.Point3d(4.0, 44.0, 0.0)
    endPoint13 = NXOpen.Point3d(4.0, 44.0, 20.0)
    line12.SetEndpoints(startPoint13, endPoint13)
    
    startPoint14 = NXOpen.Point3d(4.0, 39.0, 0.0)
    endPoint14 = NXOpen.Point3d(4.0, 44.0, 0.0)
    line11.SetEndpoints(startPoint14, endPoint14)
    
    startPoint15 = NXOpen.Point3d(4.0, 39.0, 20.0)
    endPoint15 = NXOpen.Point3d(4.0, 39.0, 0.0)
    line10.SetEndpoints(startPoint15, endPoint15)
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId25)
    
    geoms7 = [NXOpen.SmartObject.Null] * 3 
    geoms7[0] = line12
    geoms7[1] = line11
    geoms7[2] = line10
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms7)
    
    geoms8 = [NXOpen.SmartObject.Null] * 3 
    geoms8[0] = line12
    geoms8[1] = line11
    geoms8[2] = line10
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms8)
    
    geoms9 = [NXOpen.SmartObject.Null] * 3 
    geoms9[0] = line12
    geoms9[1] = line11
    geoms9[2] = line10
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms9)
    
    scaleAboutPoint6 = NXOpen.Point3d(43.304393272497165, -8.119573738593223, 0.0)
    viewCenter6 = NXOpen.Point3d(-43.304393272497194, 8.119573738593223, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(34.643514617997738, -6.4956589908745794, 0.0)
    viewCenter7 = NXOpen.Point3d(-34.643514617997766, 6.4956589908745794, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(27.900401951280319, -5.1965271926996683, 0.0)
    viewCenter8 = NXOpen.Point3d(-27.90040195128034, 5.196527192699663, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    conGeom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_13.Geometry = line10
    conGeom1_13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_13.SplineDefiningPointIndex = 0
    conGeom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_13.Geometry = line12
    conGeom2_13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint31 = theSession.ActiveSketch.CreateParallelConstraint(conGeom1_13, conGeom2_13)
    
    theSession.SetUndoMarkVisibility(markId27, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint16 = NXOpen.Point3d(4.0, 39.0, 20.0)
    endPoint16 = NXOpen.Point3d(4.0, 39.0, 0.0)
    line10.SetEndpoints(startPoint16, endPoint16)
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId27)
    
    geoms10 = [NXOpen.SmartObject.Null] * 1 
    geoms10[0] = line10
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms10)
    
    geoms11 = [NXOpen.SmartObject.Null] * 1 
    geoms11[0] = line10
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms11)
    
    geoms12 = [NXOpen.SmartObject.Null] * 1 
    geoms12[0] = line10
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms12)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId29, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    nErrs5 = theSession.UpdateManager.DoUpdate(markId29)
    
    scaleAboutPoint9 = NXOpen.Point3d(26.527034050352544, -10.195091444725053, 0.0)
    viewCenter9 = NXOpen.Point3d(-26.527034050352579, 10.195091444725048, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(32.849475468137115, -12.682000886945598, 0.0)
    viewCenter10 = NXOpen.Point3d(-32.849475468137165, 12.682000886945598, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(40.597868692966102, -15.775171834981112, 0.0)
    viewCenter11 = NXOpen.Point3d(-40.597868692966138, 15.775171834981117, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(23.295443702392415, -11.986037423637597, 0.0)
    viewCenter12 = NXOpen.Point3d(-23.295443702392483, 11.986037423637613, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(18.636354961913916, -9.5115006652091925, 0.0)
    viewCenter13 = NXOpen.Point3d(-18.63635496191398, 9.5115006652092049, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint13, viewCenter13)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketch4 = theSession.ActiveSketch
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("20")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId31, "拉伸 對話方塊")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature2 = feature3
    features2[0] = sketchFeature2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section2.AllowSelfIntersection(True)
    
    rules2 = [None] * 1 
    rules2[0] = curveFeatureRule2
    helpPoint2 = NXOpen.Point3d(4.0, -0.99999999999999334, 11.239158888368557)
    section2.AddToSection(rules2, line6, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId33, None)
    
    direction4 = workPart.Directions.CreateDirection(sketch4, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder2.Direction = direction4
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies4[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies4)
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies5 = [NXOpen.Body.Null] * 1 
    targetBodies5[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies5)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId32, None)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = body1
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies6)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId34, None)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder2.ParentFeatureInternal = False
    
    feature4 = extrudeBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId35, None)
    
    theSession.SetUndoMarkName(markId31, "拉伸")
    
    expression22 = extrudeBuilder2.Limits.StartExtend.Value
    expression23 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression19)
    
    workPart.Expressions.Delete(expression20)
    
    workPart.Expressions.Delete(expression21)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.PlaneReference = plane7
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder3 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder3.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId36, "建立草圖 對話方塊")
    
    scalar3 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge3 = extrude1.FindObject("EDGE * 120 * 140 {(19,-6,0)(-3.5,-6,0)(-26,-6,0) EXTRUDE(2)}")
    point5 = workPart.Points.CreatePoint(edge3, scalar3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction5 = workPart.Directions.CreateDirection(edge3, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face2 = extrude1.FindObject("FACE 140 {(-3.5,-6,10) EXTRUDE(2)}")
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(face2, direction5, point5, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.Csystem = cartesianCoordinateSystem3
    
    origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane8 = workPart.Planes.CreatePlane(origin8, normal8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane8.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom8 = [NXOpen.NXObject.Null] * 1 
    geom8[0] = face2
    plane8.SetGeometry(geom8)
    
    plane8.SetFlip(False)
    
    plane8.SetExpression(None)
    
    plane8.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane8.Evaluate()
    
    origin9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane9 = workPart.Planes.CreatePlane(origin9, normal9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane9.SynchronizeToPlane(plane8)
    
    scalar4 = workPart.Scalars.CreateScalar(100.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point6 = workPart.Points.CreatePoint(edge3, scalar4, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane9.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom9 = [NXOpen.NXObject.Null] * 1 
    geom9[0] = face2
    plane9.SetGeometry(geom9)
    
    plane9.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane9.Evaluate()
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId37, None)
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject4 = sketchInPlaceBuilder3.Commit()
    
    sketch5 = nXObject4
    feature5 = sketch5.Feature
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId39)
    
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId38, None)
    
    theSession.SetUndoMarkName(markId36, "建立草圖")
    
    sketchInPlaceBuilder3.Destroy()
    
    sketchAlongPathBuilder3.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression25)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point6)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression24)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane7.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression27)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression26)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane9.DestroyPlane()
    
    scaleAboutPoint14 = NXOpen.Point3d(7.8295889622148769, -1.4499238818916469, 0.0)
    viewCenter14 = NXOpen.Point3d(-7.8295889622149097, 1.4499238818916469, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(6.2636711697719027, -1.1599391055133177, 0.0)
    viewCenter15 = NXOpen.Point3d(-6.2636711697719427, 1.1599391055133113, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(5.0109369358175009, -0.92795128441066466, 0.0)
    viewCenter16 = NXOpen.Point3d(-5.0109369358175639, 0.92795128441064878, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(4.0087495486539924, -0.74236102752852762, 0.0)
    viewCenter17 = NXOpen.Point3d(-4.0087495486540599, 0.74236102752851485, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->圓(C)...
    # ----------------------------------------------
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    expression28 = workPart.Expressions.CreateSystemExpression("2")
    
    theSession.SetUndoMarkVisibility(markId41, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(-26.0, -6.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 1.0, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_16.Geometry = arc1
    geom1_16.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_16.SplineDefiningPointIndex = 0
    geom2_16 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys3 = workPart.Features.FindObject("SKETCH(5:1B)")
    point7 = datumCsys3.FindObject("POINT 1")
    geom2_16.Geometry = point7
    geom2_16.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_16.SplineDefiningPointIndex = 0
    sketchGeometricConstraint32 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_16, geom2_16)
    
    dimObject1_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_7.Geometry = arc1
    dimObject1_7.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_7.AssocValue = 0
    dimObject1_7.HelpPoint.X = 0.0
    dimObject1_7.HelpPoint.Y = 0.0
    dimObject1_7.HelpPoint.Z = 0.0
    dimObject1_7.View = NXOpen.NXObject.Null
    dimOrigin7 = NXOpen.Point3d(-26.0, -6.0, 0.44892383397000468)
    sketchDimensionalConstraint7 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_7, dimOrigin7, expression28, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    dimension7 = sketchDimensionalConstraint7.AssociatedDimension
    
    theSession.ActiveSketch.Update()
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId42, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(4.0, -6.0, 0.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 1.0, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_17 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_17.Geometry = arc2
    geom1_17.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_17.SplineDefiningPointIndex = 0
    geom2_17 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_17.Geometry = line8
    geom2_17.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_17.SplineDefiningPointIndex = 0
    sketchGeometricConstraint33 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_17, geom2_17)
    
    dimObject1_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_8.Geometry = arc2
    dimObject1_8.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_8.AssocValue = 0
    dimObject1_8.HelpPoint.X = 0.0
    dimObject1_8.HelpPoint.Y = 0.0
    dimObject1_8.HelpPoint.Z = 0.0
    dimObject1_8.View = NXOpen.NXObject.Null
    dimOrigin8 = NXOpen.Point3d(4.0, -6.0, 0.44892383397000468)
    sketchDimensionalConstraint8 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_8, dimOrigin8, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    dimension8 = sketchDimensionalConstraint8.AssociatedDimension
    
    expression29 = sketchDimensionalConstraint8.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId43, "Curve")
    
    sketch6 = theSession.ActiveSketch
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section3
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies7 = [NXOpen.Body.Null] * 1 
    targetBodies7[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies7)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies8)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder3 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId45, "拉伸 對話方塊")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features3 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature3 = feature5
    features3[0] = sketchFeature3
    curveFeatureRule3 = workPart.ScRuleFactory.CreateRuleCurveFeature(features3)
    
    section3.AllowSelfIntersection(True)
    
    rules3 = [None] * 1 
    rules3[0] = curveFeatureRule3
    helpPoint3 = NXOpen.Point3d(-26.203341671506735, -6.0, -0.97357724873470153)
    section3.AddToSection(rules3, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId47, None)
    
    direction6 = workPart.Directions.CreateDirection(sketch6, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction6
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies9)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies10)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId46, None)
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("5")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies11)
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId48, None)
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder3.ParentFeatureInternal = False
    
    feature6 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId49, None)
    
    theSession.SetUndoMarkName(markId45, "拉伸")
    
    expression33 = extrudeBuilder3.Limits.StartExtend.Value
    expression34 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression30)
    
    workPart.Expressions.Delete(expression31)
    
    workPart.Expressions.Delete(expression32)
    
    # ----------------------------------------------
    #   功能表：分析(L)->測量(S)...
    # ----------------------------------------------
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    theSession.SetUndoMarkName(markId50, "測量 對話方塊")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    scCollector1.SetMultiComponent()
    
    extrude2 = feature6
    face3 = extrude2.FindObject("FACE 160 {(4,-8.5,-1) EXTRUDE(2)}")
    line13 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line13.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    edges1 = [NXOpen.Edge.Null] * 1 
    edge4 = extrude2.FindObject("EDGE * 130 * 160 {(3.5,-11,-0.8660254037844)(5,-11,0)(3.5,-11,0.8660254037844) EXTRUDE(2)}")
    edges1[0] = edge4
    edgeDumbRule1 = workPart.ScRuleFactory.CreateRuleEdgeDumb(edges1)
    
    rules4 = [None] * 1 
    rules4[0] = edgeDumbRule1
    scCollector1.ReplaceRules(rules4, False)
    
    scCollector2 = workPart.ScCollectors.CreateCollector()
    
    scCollector2.SetMultiComponent()
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Measurement Update")
    
    nErrs7 = theSession.UpdateManager.DoUpdate(markId51)
    
    theSession.DeleteUndoMark(markId51, "Measurement Update")
    
    workPart.Features.SetEditWithRollbackFeature(NXOpen.Features.Feature.Null)
    
    scCollector1.Destroy()
    
    scCollector2.Destroy()
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line13
    nErrs8 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    theSession.UndoToMark(markId50, None)
    
    theSession.DeleteUndoMark(markId50, None)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = -0.0093848249536631935
    rotMatrix1.Xy = 0.91090530388406221
    rotMatrix1.Xz = -0.4125087301094057
    rotMatrix1.Yx = 0.16117781632339409
    rotMatrix1.Yy = 0.40851076775788925
    rotMatrix1.Yz = 0.89841007571770004
    rotMatrix1.Zx = 0.98688076107796008
    rotMatrix1.Zy = -0.05805583503615306
    rotMatrix1.Zz = -0.15065152980452468
    translation1 = NXOpen.Point3d(-7.7630882079240404, -9.4761545881258389, -2.6256779515103128)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 2.737212656172102)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Redefine Feature")
    
    editWithRollbackManager1 = workPart.Features.StartEditWithRollbackManager(extrude2, markId52)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "起點")
    
    extrudeBuilder4 = workPart.Features.CreateExtrudeBuilder(extrude2)
    
    section3.PrepareMappingData()
    
    refs1 = section3.EvaluateAndAskOutputEntities()
    
    extrudeBuilder4.AllowSelfIntersectingSection(True)
    
    targetBodies12 = [NXOpen.Body.Null] * 1 
    targetBodies12[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies12)
    
    targetBodies13 = [NXOpen.Body.Null] * 1 
    targetBodies13[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies13)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId53, "拉伸 對話方塊")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   對話開始 拉伸
    # ----------------------------------------------
    expression38 = extrudeBuilder4.Limits.StartExtend.Value
    expression39 = extrudeBuilder4.Limits.EndExtend.Value
    extrudeBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression35)
    
    workPart.Expressions.Delete(expression36)
    
    workPart.Expressions.Delete(expression37)
    
    theSession.UndoToMark(markId53, None)
    
    theSession.DeleteUndoMark(markId53, None)
    
    theSession.DeleteUndoMark(markId53, None)
    
    editWithRollbackManager1.UpdateFeature(True)
    
    editWithRollbackManager1.Stop()
    
    theSession.UndoToMarkWithStatus(markId52, None)
    
    theSession.DeleteUndoMarksUpToMark(markId52, None, False)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = -0.92057946055510964
    rotMatrix2.Xy = 0.29964134635651851
    rotMatrix2.Xz = -0.25049654759640644
    rotMatrix2.Yx = -0.25506385705687462
    rotMatrix2.Yy = 0.024453105857195116
    rotMatrix2.Yz = 0.96661495665917008
    rotMatrix2.Zx = 0.29576322561693769
    rotMatrix2.Zy = 0.95373849097516883
    rotMatrix2.Zz = 0.053916650536494609
    translation2 = NXOpen.Point3d(-2.8611271849988507, -5.4521162292294267, -24.028152185780897)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 2.737212656172102)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder4 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal10 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane10 = workPart.Planes.CreatePlane(origin10, normal10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder4.PlaneReference = plane10
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder4 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder4.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId54, "建立草圖 對話方塊")
    
    scalar5 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point8 = workPart.Points.CreatePoint(line1, scalar5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumAxis2 = workPart.Datums.FindObject("SKETCH(1:1B) X axis")
    direction7 = workPart.Directions.CreateDirection(datumAxis2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane2 = workPart.Datums.FindObject("SKETCH(1:1B) XY plane")
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane2, direction7, point8, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder4.Csystem = cartesianCoordinateSystem4
    
    origin11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal11 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane11 = workPart.Planes.CreatePlane(origin11, normal11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane11.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom10 = [NXOpen.NXObject.Null] * 1 
    geom10[0] = datumPlane2
    plane11.SetGeometry(geom10)
    
    plane11.SetFlip(False)
    
    plane11.SetExpression(None)
    
    plane11.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane11.Evaluate()
    
    origin12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal12 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane12 = workPart.Planes.CreatePlane(origin12, normal12, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane12.SynchronizeToPlane(plane11)
    
    scalar6 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point9 = workPart.Points.CreatePoint(line1, scalar6, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane12.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom11 = [NXOpen.NXObject.Null] * 1 
    geom11[0] = datumPlane2
    plane12.SetGeometry(geom11)
    
    plane12.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane12.Evaluate()
    
    sketchInPlaceBuilder4.Destroy()
    
    sketchAlongPathBuilder4.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression41)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point9)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression40)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane10.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression43)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression42)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane12.DestroyPlane()
    
    theSession.UndoToMark(markId54, None)
    
    theSession.DeleteUndoMark(markId54, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder5 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal13 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane13 = workPart.Planes.CreatePlane(origin13, normal13, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder5.PlaneReference = plane13
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder5 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder5.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId55, "建立草圖 對話方塊")
    
    scalar7 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge5 = extrude1.FindObject("EDGE * 120 * 160 {(-26,44,0)(-3.5,44,0)(19,44,0) EXTRUDE(2)}")
    point10 = workPart.Points.CreatePoint(edge5, scalar7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction8 = workPart.Directions.CreateDirection(edge5, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face4 = extrude1.FindObject("FACE 160 {(-3.5,44,10) EXTRUDE(2)}")
    xform5 = workPart.Xforms.CreateXformByPlaneXDirPoint(face4, direction8, point10, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem5 = workPart.CoordinateSystems.CreateCoordinateSystem(xform5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder5.Csystem = cartesianCoordinateSystem5
    
    origin14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal14 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane14 = workPart.Planes.CreatePlane(origin14, normal14, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane14.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom12 = [NXOpen.NXObject.Null] * 1 
    geom12[0] = face4
    plane14.SetGeometry(geom12)
    
    plane14.SetFlip(False)
    
    plane14.SetExpression(None)
    
    plane14.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane14.Evaluate()
    
    origin15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal15 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane15 = workPart.Planes.CreatePlane(origin15, normal15, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression47 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane15.SynchronizeToPlane(plane14)
    
    scalar8 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point11 = workPart.Points.CreatePoint(edge5, scalar8, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane15.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom13 = [NXOpen.NXObject.Null] * 1 
    geom13[0] = face4
    plane15.SetGeometry(geom13)
    
    plane15.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane15.Evaluate()
    
    scaleAboutPoint18 = NXOpen.Point3d(45.334286707145466, 2.6098629874049641, 0.0)
    viewCenter18 = NXOpen.Point3d(-45.334286707145502, -2.6098629874049641, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(35.416807355006611, 1.1599391055133177, 0.0)
    viewCenter19 = NXOpen.Point3d(-35.41680735500664, -1.1599391055133177, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(28.085992208162452, 0.43304393272496838, 0.0)
    viewCenter20 = NXOpen.Point3d(-28.085992208162473, -0.43304393272497893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(22.468793766529938, 0.29694441101140501, 0.0)
    viewCenter21 = NXOpen.Point3d(-22.468793766529988, -0.29694441101141344, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.DeleteUndoMark(markId56, None)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "建立草圖")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject5 = sketchInPlaceBuilder5.Commit()
    
    sketch7 = nXObject5
    feature7 = sketch7.Feature
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs9 = theSession.UpdateManager.DoUpdate(markId58)
    
    sketch7.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId57, None)
    
    theSession.SetUndoMarkName(markId55, "建立草圖")
    
    sketchInPlaceBuilder5.Destroy()
    
    sketchAlongPathBuilder5.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression45)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point11)
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression44)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane13.DestroyPlane()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression47)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression46)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane15.DestroyPlane()
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketch8 = theSession.ActiveSketch
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖(H)...
    # ----------------------------------------------
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchInPlaceBuilder6 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal16 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane16 = workPart.Planes.CreatePlane(origin16, normal16, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder6.PlaneReference = plane16
    
    expression48 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression49 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder6 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder6.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId60, "建立草圖 對話方塊")
    
    sketchInPlaceBuilder6.Destroy()
    
    sketchAlongPathBuilder6.Destroy()
    
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression49)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # 運算式仍然在使用中。
        workPart.Expressions.Delete(expression48)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane16.DestroyPlane()
    
    theSession.UndoToMark(markId60, None)
    
    theSession.DeleteUndoMark(markId60, None)
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Enter Direct Sketch")
    
    theSession.SetUndoMarkVisibility(markId61, "Enter Direct Sketch", NXOpen.Session.MarkVisibility.Visible)
    
    sketch8.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    # ----------------------------------------------
    #   功能表：插入(S)->草圖曲線(S)->圓(C)...
    # ----------------------------------------------
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    expression50 = workPart.Expressions.CreateSystemExpression("2")
    
    theSession.SetUndoMarkVisibility(markId63, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix3 = theSession.ActiveSketch.Orientation
    
    center3 = NXOpen.Point3d(-26.000000000000004, 44.0, 0.0)
    arc3 = workPart.Curves.CreateArc(center3, nXMatrix3, 1.0, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_18 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_18.Geometry = arc3
    geom1_18.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_18.SplineDefiningPointIndex = 0
    geom2_18 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys4 = workPart.Features.FindObject("SKETCH(7:1B)")
    point12 = datumCsys4.FindObject("POINT 1")
    geom2_18.Geometry = point12
    geom2_18.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_18.SplineDefiningPointIndex = 0
    sketchGeometricConstraint34 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_18, geom2_18)
    
    dimObject1_9 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_9.Geometry = arc3
    dimObject1_9.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_9.AssocValue = 0
    dimObject1_9.HelpPoint.X = 0.0
    dimObject1_9.HelpPoint.Y = 0.0
    dimObject1_9.HelpPoint.Z = 0.0
    dimObject1_9.View = NXOpen.NXObject.Null
    dimOrigin9 = NXOpen.Point3d(-26.000000000000004, 44.0, 0.44892383397000463)
    sketchDimensionalConstraint9 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_9, dimOrigin9, expression50, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    dimension9 = sketchDimensionalConstraint9.AssociatedDimension
    
    theSession.ActiveSketch.Update()
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId64, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix4 = theSession.ActiveSketch.Orientation
    
    center4 = NXOpen.Point3d(4.0, 44.0, 0.0)
    arc4 = workPart.Curves.CreateArc(center4, nXMatrix4, 1.0, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_19 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_19.Geometry = arc4
    geom1_19.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_19.SplineDefiningPointIndex = 0
    geom2_19 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_19.Geometry = line1
    geom2_19.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_19.SplineDefiningPointIndex = 0
    sketchGeometricConstraint35 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_19, geom2_19)
    
    dimObject1_10 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_10.Geometry = arc4
    dimObject1_10.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_10.AssocValue = 0
    dimObject1_10.HelpPoint.X = 0.0
    dimObject1_10.HelpPoint.Y = 0.0
    dimObject1_10.HelpPoint.Z = 0.0
    dimObject1_10.View = NXOpen.NXObject.Null
    dimOrigin10 = NXOpen.Point3d(4.0, 44.0, 0.44892383397000463)
    sketchDimensionalConstraint10 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_10, dimOrigin10, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsDriving)
    
    dimension10 = sketchDimensionalConstraint10.AssociatedDimension
    
    expression51 = sketchDimensionalConstraint10.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.DeleteUndoMark(markId65, "Curve")
    
    # ----------------------------------------------
    #   功能表：檔案(F)->完成草圖(K)
    # ----------------------------------------------
    sketch9 = theSession.ActiveSketch
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder5 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section4 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder5.Section = section4
    
    extrudeBuilder5.AllowSelfIntersectingSection(True)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder5.DistanceTolerance = 0.01
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies14 = [NXOpen.Body.Null] * 1 
    targetBodies14[0] = NXOpen.Body.Null
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies14)
    
    extrudeBuilder5.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("5")
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies15 = [NXOpen.Body.Null] * 1 
    targetBodies15[0] = NXOpen.Body.Null
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies15)
    
    extrudeBuilder5.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder5.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder5.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder5.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder4 = extrudeBuilder5.SmartVolumeProfile
    
    smartVolumeProfileBuilder4.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder4.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId67, "拉伸 對話方塊")
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    section4.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features4 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature4 = feature7
    features4[0] = sketchFeature4
    curveFeatureRule4 = workPart.ScRuleFactory.CreateRuleCurveFeature(features4)
    
    section4.AllowSelfIntersection(True)
    
    rules5 = [None] * 1 
    rules5[0] = curveFeatureRule4
    helpPoint4 = NXOpen.Point3d(3.5156976781074762, 44.0, -0.87223204221010575)
    section4.AddToSection(rules5, arc4, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint4, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId69, None)
    
    direction9 = workPart.Directions.CreateDirection(sketch9, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder5.Direction = direction9
    
    targetBodies16 = [NXOpen.Body.Null] * 1 
    targetBodies16[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies16)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies17 = [NXOpen.Body.Null] * 1 
    targetBodies17[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies17)
    
    expression53 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression54 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId68, None)
    
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId70, None)
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder5.ParentFeatureInternal = False
    
    feature8 = extrudeBuilder5.CommitFeature()
    
    theSession.DeleteUndoMark(markId71, None)
    
    theSession.SetUndoMarkName(markId67, "拉伸")
    
    expression55 = extrudeBuilder5.Limits.StartExtend.Value
    expression56 = extrudeBuilder5.Limits.EndExtend.Value
    extrudeBuilder5.Destroy()
    
    workPart.Expressions.Delete(expression52)
    
    workPart.Expressions.Delete(expression53)
    
    workPart.Expressions.Delete(expression54)
    
    scaleAboutPoint22 = NXOpen.Point3d(-3.8800736372157703, -6.8891103354647019, 0.0)
    viewCenter22 = NXOpen.Point3d(3.8800736372157298, 6.8891103354646885, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(-4.8995827816882782, -8.6113879193308733, 0.0)
    viewCenter23 = NXOpen.Point3d(4.8995827816882276, 8.6113879193308644, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(-6.2482053150317594, -10.764234899163588, 0.0)
    viewCenter24 = NXOpen.Point3d(6.2482053150317176, 10.764234899163577, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(-7.964915191191472, -13.455293623954484, 0.0)
    viewCenter25 = NXOpen.Point3d(7.9649151911914124, 13.455293623954477, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint25, viewCenter25)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.604123551829573
    rotMatrix3.Xy = 0.78467256072470537
    rotMatrix3.Xz = 0.13900973552437704
    rotMatrix3.Yx = -0.23723762006435395
    rotMatrix3.Yy = 0.010561829746522229
    rotMatrix3.Yz = 0.97139423478761155
    rotMatrix3.Zx = 0.76075820452429255
    rotMatrix3.Zy = -0.61982047416824015
    rotMatrix3.Zz = 0.19253450093641994
    translation3 = NXOpen.Point3d(-41.687588136753796, -15.992244959186086, 6.4125784887739954)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 2.7372126561721029)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.53193349542412716
    rotMatrix4.Xy = 0.83844929058553297
    rotMatrix4.Xz = 0.11853077053022733
    rotMatrix4.Yx = -0.31461449092802068
    rotMatrix4.Yy = 0.065731283559084086
    rotMatrix4.Yz = 0.94694092765060101
    rotMatrix4.Zx = 0.78617076932685293
    rotMatrix4.Zy = -0.54100109563502297
    rotMatrix4.Zz = 0.29875296814882574
    translation4 = NXOpen.Point3d(-42.803556062286873, -17.117665647277818, 4.007585117335255)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 2.7372126561721029)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->儲存(S)
    # ----------------------------------------------
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    theSession.SetUndoMarkName(markId72, "命名零件 對話方塊")
    
    theSession.UndoToMark(markId72, None)
    
    theSession.DeleteUndoMark(markId72, None)
    
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()