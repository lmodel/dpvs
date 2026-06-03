---
search:
  boost: 10.0
---

# Class: HighVolumeOfProcesses 


_Justification that the process is delayed due to high volume of similar_

_processes required to be fulfilled_



<div data-search-exclude markdown="1">



URI: [justifications:HighVolumeOfProcesses](https://w3id.org/lmodel/dpv/justifications/HighVolumeOfProcesses)





```mermaid
 classDiagram
    class HighVolumeOfProcesses
    click HighVolumeOfProcesses href "../HighVolumeOfProcesses/"
      DelayJustification <|-- HighVolumeOfProcesses
        click DelayJustification href "../DelayJustification/"
      
      
```





## Inheritance
* [DelayJustification](DelayJustification.md)
    * **HighVolumeOfProcesses**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:HighVolumeOfProcesses](https://w3id.org/lmodel/dpv/justifications/HighVolumeOfProcesses) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* High Volume Of Processes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#HighVolumeOfProcesses |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:HighVolumeOfProcesses |
| native | justifications:HighVolumeOfProcesses |
| exact | dpv_justifications:HighVolumeOfProcesses, dpv_justifications_owl:HighVolumeOfProcesses |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HighVolumeOfProcesses
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#HighVolumeOfProcesses
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is delayed due to high volume of similar

  processes required to be fulfilled'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- High Volume Of Processes
exact_mappings:
- dpv_justifications:HighVolumeOfProcesses
- dpv_justifications_owl:HighVolumeOfProcesses
is_a: DelayJustification
class_uri: justifications:HighVolumeOfProcesses

```
</details>

### Induced

<details>
```yaml
name: HighVolumeOfProcesses
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#HighVolumeOfProcesses
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process is delayed due to high volume of similar

  processes required to be fulfilled'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- High Volume Of Processes
exact_mappings:
- dpv_justifications:HighVolumeOfProcesses
- dpv_justifications_owl:HighVolumeOfProcesses
is_a: DelayJustification
class_uri: justifications:HighVolumeOfProcesses

```
</details></div>