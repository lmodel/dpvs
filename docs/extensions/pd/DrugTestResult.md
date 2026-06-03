---
search:
  boost: 10.0
---

# Class: DrugTestResult 


_Information about drug test results_



<div data-search-exclude markdown="1">



URI: [pd:DrugTestResult](https://w3id.org/lmodel/dpv/pd/DrugTestResult)





```mermaid
 classDiagram
    class DrugTestResult
    click DrugTestResult href "../DrugTestResult/"
      MedicalHealth <|-- DrugTestResult
        click MedicalHealth href "../MedicalHealth/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **DrugTestResult**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DrugTestResult](https://w3id.org/lmodel/dpv/pd/DrugTestResult) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Drug Test Result




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DrugTestResult |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DrugTestResult |
| native | pd:DrugTestResult |
| exact | dpv_pd:DrugTestResult, dpv_pd_owl:DrugTestResult |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DrugTestResult
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DrugTestResult
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about drug test results
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Drug Test Result
exact_mappings:
- dpv_pd:DrugTestResult
- dpv_pd_owl:DrugTestResult
is_a: MedicalHealth
class_uri: pd:DrugTestResult

```
</details>

### Induced

<details>
```yaml
name: DrugTestResult
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DrugTestResult
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about drug test results
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Drug Test Result
exact_mappings:
- dpv_pd:DrugTestResult
- dpv_pd_owl:DrugTestResult
is_a: MedicalHealth
class_uri: pd:DrugTestResult

```
</details></div>