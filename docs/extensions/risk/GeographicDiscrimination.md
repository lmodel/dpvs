---
search:
  boost: 10.0
---

# Class: GeographicDiscrimination 


_Discrimination based on a person's geographical origin or residence_



<div data-search-exclude markdown="1">



URI: [risk:GeographicDiscrimination](https://w3id.org/lmodel/dpv/risk/GeographicDiscrimination)





```mermaid
 classDiagram
    class GeographicDiscrimination
    click GeographicDiscrimination href "../GeographicDiscrimination/"
      PotentialConsequence <|-- GeographicDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- GeographicDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- GeographicDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- GeographicDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **GeographicDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:GeographicDiscrimination](https://w3id.org/lmodel/dpv/risk/GeographicDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Geographic Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#GeographicDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:GeographicDiscrimination |
| native | risk:GeographicDiscrimination |
| exact | dpv_risk:GeographicDiscrimination, dpv_risk_owl:GeographicDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeographicDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GeographicDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's geographical origin or residence
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Geographic Discrimination
exact_mappings:
- dpv_risk:GeographicDiscrimination
- dpv_risk_owl:GeographicDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GeographicDiscrimination

```
</details>

### Induced

<details>
```yaml
name: GeographicDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GeographicDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's geographical origin or residence
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Geographic Discrimination
exact_mappings:
- dpv_risk:GeographicDiscrimination
- dpv_risk_owl:GeographicDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GeographicDiscrimination

```
</details></div>