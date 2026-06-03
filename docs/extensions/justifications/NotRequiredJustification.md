---
search:
  boost: 10.0
---

# Class: NotRequiredJustification 


_Justification to reject or not complete a process as it is not required_

_or isn't applicable_



<div data-search-exclude markdown="1">



URI: [justifications:NotRequiredJustification](https://w3id.org/lmodel/dpv/justifications/NotRequiredJustification)





```mermaid
 classDiagram
    class NotRequiredJustification
    click NotRequiredJustification href "../NotRequiredJustification/"
      NotRequiredJustification <|-- ProcessSafeguarded
        click ProcessSafeguarded href "../ProcessSafeguarded/"
      NotRequiredJustification <|-- RightsFreedomsImpactUnlikely
        click RightsFreedomsImpactUnlikely href "../RightsFreedomsImpactUnlikely/"
      NotRequiredJustification <|-- RiskMitigated
        click RiskMitigated href "../RiskMitigated/"
      
      
```





## Inheritance
* **NotRequiredJustification**
    * [ProcessSafeguarded](ProcessSafeguarded.md)
    * [RightsFreedomsImpactUnlikely](RightsFreedomsImpactUnlikely.md)
    * [RiskMitigated](RiskMitigated.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:NotRequiredJustification](https://w3id.org/lmodel/dpv/justifications/NotRequiredJustification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Not Required Justification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#NotRequiredJustification |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:NotRequiredJustification |
| native | justifications:NotRequiredJustification |
| exact | dpv_justifications:NotRequiredJustification, dpv_justifications_owl:NotRequiredJustification |
| related | oscal:RiskAcceptance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NotRequiredJustification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#NotRequiredJustification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification to reject or not complete a process as it is not required

  or isn''t applicable'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Not Required Justification
exact_mappings:
- dpv_justifications:NotRequiredJustification
- dpv_justifications_owl:NotRequiredJustification
related_mappings:
- oscal:RiskAcceptance
class_uri: justifications:NotRequiredJustification

```
</details>

### Induced

<details>
```yaml
name: NotRequiredJustification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#NotRequiredJustification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification to reject or not complete a process as it is not required

  or isn''t applicable'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Not Required Justification
exact_mappings:
- dpv_justifications:NotRequiredJustification
- dpv_justifications_owl:NotRequiredJustification
related_mappings:
- oscal:RiskAcceptance
class_uri: justifications:NotRequiredJustification

```
</details></div>