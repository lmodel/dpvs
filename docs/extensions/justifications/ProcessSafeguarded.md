---
search:
  boost: 10.0
---

# Class: ProcessSafeguarded 


_Justification that the process is not required as it is safeguarded by_

_appropriate technical and organisational measures_



<div data-search-exclude markdown="1">



URI: [justifications:ProcessSafeguarded](https://w3id.org/lmodel/dpv/justifications/ProcessSafeguarded)





```mermaid
 classDiagram
    class ProcessSafeguarded
    click ProcessSafeguarded href "../ProcessSafeguarded/"
      NotRequiredJustification <|-- ProcessSafeguarded
        click NotRequiredJustification href "../NotRequiredJustification/"
      
      
```





## Inheritance
* [NotRequiredJustification](NotRequiredJustification.md)
    * **ProcessSafeguarded**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ProcessSafeguarded](https://w3id.org/lmodel/dpv/justifications/ProcessSafeguarded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Process Safeguarded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ProcessSafeguarded |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ProcessSafeguarded |
| native | justifications:ProcessSafeguarded |
| exact | dpv_justifications:ProcessSafeguarded, dpv_justifications_owl:ProcessSafeguarded |
| close | oscal:RiskMitigatingFactor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessSafeguarded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessSafeguarded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is not required as it is safeguarded
  by

  appropriate technical and organisational measures'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Safeguarded
exact_mappings:
- dpv_justifications:ProcessSafeguarded
- dpv_justifications_owl:ProcessSafeguarded
close_mappings:
- oscal:RiskMitigatingFactor
is_a: NotRequiredJustification
class_uri: justifications:ProcessSafeguarded

```
</details>

### Induced

<details>
```yaml
name: ProcessSafeguarded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessSafeguarded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is not required as it is safeguarded
  by

  appropriate technical and organisational measures'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Safeguarded
exact_mappings:
- dpv_justifications:ProcessSafeguarded
- dpv_justifications_owl:ProcessSafeguarded
close_mappings:
- oscal:RiskMitigatingFactor
is_a: NotRequiredJustification
class_uri: justifications:ProcessSafeguarded

```
</details></div>