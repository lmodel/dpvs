---
search:
  boost: 10.0
---

# Class: RiskMitigated 


_Justification that the process is not required as the risks have been_

_effectively mitigated by technical and organisational measures_



<div data-search-exclude markdown="1">



URI: [justifications:RiskMitigated](https://w3id.org/lmodel/dpv/justifications/RiskMitigated)





```mermaid
 classDiagram
    class RiskMitigated
    click RiskMitigated href "../RiskMitigated/"
      NotRequiredJustification <|-- RiskMitigated
        click NotRequiredJustification href "../NotRequiredJustification/"
      
      
```





## Inheritance
* [NotRequiredJustification](NotRequiredJustification.md)
    * **RiskMitigated**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:RiskMitigated](https://w3id.org/lmodel/dpv/justifications/RiskMitigated) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Risk Mitigated




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#RiskMitigated |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:RiskMitigated |
| native | justifications:RiskMitigated |
| exact | dpv_justifications:RiskMitigated, dpv_justifications_owl:RiskMitigated |
| close | oscal:RiskMitigatingFactor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskMitigated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#RiskMitigated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is not required as the risks have been

  effectively mitigated by technical and organisational measures'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Risk Mitigated
exact_mappings:
- dpv_justifications:RiskMitigated
- dpv_justifications_owl:RiskMitigated
close_mappings:
- oscal:RiskMitigatingFactor
is_a: NotRequiredJustification
class_uri: justifications:RiskMitigated

```
</details>

### Induced

<details>
```yaml
name: RiskMitigated
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#RiskMitigated
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is not required as the risks have been

  effectively mitigated by technical and organisational measures'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Risk Mitigated
exact_mappings:
- dpv_justifications:RiskMitigated
- dpv_justifications_owl:RiskMitigated
close_mappings:
- oscal:RiskMitigatingFactor
is_a: NotRequiredJustification
class_uri: justifications:RiskMitigated

```
</details></div>