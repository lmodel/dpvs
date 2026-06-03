---
search:
  boost: 10.0
---

# Class: ViolenceAgainstChildren 


_Concept representing Child Violence_



<div data-search-exclude markdown="1">



URI: [risk:ViolenceAgainstChildren](https://w3id.org/lmodel/dpv/risk/ViolenceAgainstChildren)





```mermaid
 classDiagram
    class ViolenceAgainstChildren
    click ViolenceAgainstChildren href "../ViolenceAgainstChildren/"
      PotentialConsequence <|-- ViolenceAgainstChildren
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ViolenceAgainstChildren
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ViolenceAgainstChildren
        click PotentialRisk href "../PotentialRisk/"
      Harm <|-- ViolenceAgainstChildren
        click Harm href "../Harm/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * **ViolenceAgainstChildren** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ViolenceAgainstChildren](https://w3id.org/lmodel/dpv/risk/ViolenceAgainstChildren) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Violence against children


## Comments

* This concept was called "ChildViolence" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ViolenceAgainstChildren |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ViolenceAgainstChildren |
| native | risk:ViolenceAgainstChildren |
| exact | dpv_risk:ViolenceAgainstChildren, dpv_risk_owl:ViolenceAgainstChildren |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ViolenceAgainstChildren
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolenceAgainstChildren
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Child Violence
comments:
- This concept was called "ChildViolence" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violence against children
exact_mappings:
- dpv_risk:ViolenceAgainstChildren
- dpv_risk_owl:ViolenceAgainstChildren
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ViolenceAgainstChildren

```
</details>

### Induced

<details>
```yaml
name: ViolenceAgainstChildren
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ViolenceAgainstChildren
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Child Violence
comments:
- This concept was called "ChildViolence" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Violence against children
exact_mappings:
- dpv_risk:ViolenceAgainstChildren
- dpv_risk_owl:ViolenceAgainstChildren
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ViolenceAgainstChildren

```
</details></div>