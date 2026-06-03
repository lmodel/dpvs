---
search:
  boost: 10.0
---

# Class: DelayJustification 


_Justification to delay a process_



<div data-search-exclude markdown="1">



URI: [justifications:DelayJustification](https://w3id.org/lmodel/dpv/justifications/DelayJustification)





```mermaid
 classDiagram
    class DelayJustification
    click DelayJustification href "../DelayJustification/"
      DelayJustification <|-- ComplexityOfProcess
        click ComplexityOfProcess href "../ComplexityOfProcess/"
      DelayJustification <|-- HighVolumeOfProcesses
        click HighVolumeOfProcesses href "../HighVolumeOfProcesses/"
      DelayJustification <|-- IdentityVerificationRequired
        click IdentityVerificationRequired href "../IdentityVerificationRequired/"
      DelayJustification <|-- InformationRequired
        click InformationRequired href "../InformationRequired/"
      
      
```





## Inheritance
* **DelayJustification**
    * [ComplexityOfProcess](ComplexityOfProcess.md)
    * [HighVolumeOfProcesses](HighVolumeOfProcesses.md)
    * [IdentityVerificationRequired](IdentityVerificationRequired.md)
    * [InformationRequired](InformationRequired.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:DelayJustification](https://w3id.org/lmodel/dpv/justifications/DelayJustification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Delay Justification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#DelayJustification |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:DelayJustification |
| native | justifications:DelayJustification |
| exact | dpv_justifications:DelayJustification, dpv_justifications_owl:DelayJustification |
| related | oscal:ResponsibilityStatement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DelayJustification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DelayJustification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: Justification to delay a process
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Delay Justification
exact_mappings:
- dpv_justifications:DelayJustification
- dpv_justifications_owl:DelayJustification
related_mappings:
- oscal:ResponsibilityStatement
class_uri: justifications:DelayJustification

```
</details>

### Induced

<details>
```yaml
name: DelayJustification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DelayJustification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: Justification to delay a process
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Delay Justification
exact_mappings:
- dpv_justifications:DelayJustification
- dpv_justifications_owl:DelayJustification
related_mappings:
- oscal:ResponsibilityStatement
class_uri: justifications:DelayJustification

```
</details></div>