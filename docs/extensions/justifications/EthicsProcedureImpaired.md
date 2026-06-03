---
search:
  boost: 10.0
---

# Class: EthicsProcedureImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would compromise ethics or ethics procedures_



<div data-search-exclude markdown="1">



URI: [justifications:EthicsProcedureImpaired](https://w3id.org/lmodel/dpv/justifications/EthicsProcedureImpaired)





```mermaid
 classDiagram
    class EthicsProcedureImpaired
    click EthicsProcedureImpaired href "../EthicsProcedureImpaired/"
      NonFulfilmentJustification <|-- EthicsProcedureImpaired
        click NonFulfilmentJustification href "../NonFulfilmentJustification/"
      

      EthicsProcedureImpaired <|-- EthicsBreachDetectionImpaired
        click EthicsBreachDetectionImpaired href "../EthicsBreachDetectionImpaired/"
      EthicsProcedureImpaired <|-- EthicsBreachInvestigationImpaired
        click EthicsBreachInvestigationImpaired href "../EthicsBreachInvestigationImpaired/"
      EthicsProcedureImpaired <|-- EthicsBreachPreventionImpaired
        click EthicsBreachPreventionImpaired href "../EthicsBreachPreventionImpaired/"
      EthicsProcedureImpaired <|-- EthicsBreachProsecutionImpaired
        click EthicsBreachProsecutionImpaired href "../EthicsBreachProsecutionImpaired/"
      

      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * **EthicsProcedureImpaired**
        * [EthicsBreachDetectionImpaired](EthicsBreachDetectionImpaired.md)
        * [EthicsBreachInvestigationImpaired](EthicsBreachInvestigationImpaired.md)
        * [EthicsBreachPreventionImpaired](EthicsBreachPreventionImpaired.md)
        * [EthicsBreachProsecutionImpaired](EthicsBreachProsecutionImpaired.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:EthicsProcedureImpaired](https://w3id.org/lmodel/dpv/justifications/EthicsProcedureImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Ethics Procedure Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#EthicsProcedureImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:EthicsProcedureImpaired |
| native | justifications:EthicsProcedureImpaired |
| exact | dpv_justifications:EthicsProcedureImpaired, dpv_justifications_owl:EthicsProcedureImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EthicsProcedureImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#EthicsProcedureImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would compromise ethics or ethics procedures'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Ethics Procedure Impaired
exact_mappings:
- dpv_justifications:EthicsProcedureImpaired
- dpv_justifications_owl:EthicsProcedureImpaired
is_a: NonFulfilmentJustification
class_uri: justifications:EthicsProcedureImpaired

```
</details>

### Induced

<details>
```yaml
name: EthicsProcedureImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#EthicsProcedureImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would compromise ethics or ethics procedures'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Ethics Procedure Impaired
exact_mappings:
- dpv_justifications:EthicsProcedureImpaired
- dpv_justifications_owl:EthicsProcedureImpaired
is_a: NonFulfilmentJustification
class_uri: justifications:EthicsProcedureImpaired

```
</details></div>