---
search:
  boost: 10.0
---

# Class: TechnologyOverreliance 


_Concept representing the case where an entity, including individuals,_

_have an overreliance on the use of technology_



<div data-search-exclude markdown="1">



URI: [risk:TechnologyOverreliance](https://w3id.org/lmodel/dpv/risk/TechnologyOverreliance)





```mermaid
 classDiagram
    class TechnologyOverreliance
    click TechnologyOverreliance href "../TechnologyOverreliance/"
      PotentialConsequence <|-- TechnologyOverreliance
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- TechnologyOverreliance
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- TechnologyOverreliance
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalManagementRisk <|-- TechnologyOverreliance
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **TechnologyOverreliance** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:TechnologyOverreliance](https://w3id.org/lmodel/dpv/risk/TechnologyOverreliance) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Technology Overreliance




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#TechnologyOverreliance |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:TechnologyOverreliance |
| native | risk:TechnologyOverreliance |
| exact | dpv_risk:TechnologyOverreliance, dpv_risk_owl:TechnologyOverreliance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TechnologyOverreliance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TechnologyOverreliance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing the case where an entity, including individuals,

  have an overreliance on the use of technology'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Technology Overreliance
exact_mappings:
- dpv_risk:TechnologyOverreliance
- dpv_risk_owl:TechnologyOverreliance
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TechnologyOverreliance

```
</details>

### Induced

<details>
```yaml
name: TechnologyOverreliance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TechnologyOverreliance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing the case where an entity, including individuals,

  have an overreliance on the use of technology'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Technology Overreliance
exact_mappings:
- dpv_risk:TechnologyOverreliance
- dpv_risk_owl:TechnologyOverreliance
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TechnologyOverreliance

```
</details></div>